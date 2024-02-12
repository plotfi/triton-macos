clang dummy-ptxas.c -o dummy-ptxas

export TRITON_PTXAS_PATH=`pwd`/dummy-ptxas
export LLVM_IR_ENABLE_DUMP=1
export MLIR_ENABLE_DUMP=1

python offline-compile.py
