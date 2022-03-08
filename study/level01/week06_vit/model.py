import torch
import torch.nn as nn

from einops import rearrange
from einops.layers.torch import Reduce

class MultiHeadAttention(nn.Module):
    def __init__(self, emb_size: int, num_heads: int = 8) -> None:
        super().__init__()

        self.emb_size = emb_size
        self.num_heads = num_heads
        self.w_qkv = nn.Linear(emb_size, emb_size * 3)
        self.projection = nn.Linear(emb_size, emb_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        w = self.w_qkv(x)
        w = rearrange(w, "b n (h d w) -> w b h n d", h=self.num_heads, w=3)
        q, k, v = w[0], w[1], w[2]
        q_k = torch.einsum('bhqd, bhkd -> bhqk', q, k) # batch, num_heads, query_len, key_len
        q_k = nn.Softmax(q_k, dim=-1) / (self.emb_size ** 0.5)
        x = torch.einsum('bhal, bhlv -> bhav', q_k, v)
        x = rearrange(x, "b h n d -> b n (h d)")
        return self.projection(x)

class FeedForwardBlock(nn.Module):
    def __init__(self, emb_size: int, expansion: int = 4) -> None:
        super().__init__()

        self.lin1 = nn.Linear(emb_size, emb_size * expansion)
        self.gelu = nn.GELU()
        self.lin2 = nn.Linear(emb_size * expansion, emb_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.lin1(x)
        x = self.gelu(x)
        return self.lin2(x)

class TransformerEncoderBlock(nn.Module):
    def __init__(self, emb_size: int) -> None:
        super().__init__()

        self.mha = MultiHeadAttention(emb_size)
        self.ff = FeedForwardBlock(emb_size)
        self.ln = nn.LayerNorm(emb_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.mha(x)
        x = self.ln(x)
        x = x + self.ff(x)
        return self.ln(x)

class ViT(nn.Module):
    def __init__(self, img_size: int = 224, patch_size: int = 16, channels: int = 3, classes: int = 1000, depth: int = 12) -> None:
        super().__init__()

        emb_size = patch_size * patch_size * channels

        self.projection = rearrange('b c (vn ps) (hn ps) -> b (vn hn) emb', ps=patch_size, emb=emb_size)
        self.cls_token = nn.Parameter(torch.randn(1, 1, emb_size))
        self.pos_emb = nn.Parameter(torch.randn((img_size // patch_size) ** 2 + 1, emb_size))
        self.transformer_enc = nn.Sequential(
            *[TransformerEncoderBlock(emb_size=emb_size) for _ in range(depth)]
        )
        self.mlp_head = nn.Sequential(
            Reduce('b n e -> b e', reduction='mean'),
            nn.LayerNorm(emb_size),
            nn.Linear(emb_size, classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.projection(x)
        x = torch.cat([self.cls_token, x], dim=1)
        x += self.pos_emb
        x = self.transformer_enc(x)
        return self.mlp_head(x)
