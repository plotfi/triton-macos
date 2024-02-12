import triton
import triton.language as tl

@triton.jit
def triton_(src0, src1, dst):
    offset = tl.load(src0, None)
    val = tl.load(src1, None)
    tl.atomic_add(dst + offset, val)

major, minor = (9, 0)
capability = major * 10 + minor
options = {"num_warps": 4, "num_ctas": 1, "num_stages": 3, "ptx_version": 81}

src = triton.compiler.ASTSource(fn=triton_, signature="*i32,*i32,*i32")
ret = triton.compile(src, target=("cuda", capability), options=options)
print(ret.asm["ttgir"])

