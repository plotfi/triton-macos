# triton-macos
Some env var and build system hacks to get triton building and dumping IR on macOS

### Purpose???

Why did I do this? Because I like to do local development on my M1/2/3 laptop some of the times. I find it a little easier to get stuff done.

### Instructions
* Apply the CMakeLists-LLVMAArch64.patch to your Triton repo so that your build links with Native
* source run.sh

This should generate your dummy-ptxas and set environment variables needed to run and dump IRs from Triton.

offline-compile.py is an example Triton kernel and compile invocation that uses Triton's compile API to set the proper warp, ctas, stages, ptx version, Cuda capabilities etc to do a compile run on a non-supported system like a Mac.

