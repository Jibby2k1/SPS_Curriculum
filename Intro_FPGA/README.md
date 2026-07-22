# Introduction to FPGA Systems

Application track: pushing signal processing into hardware. Where
[GPU workshops](../Intro_GPU/README.md) parallelize software, FPGAs let you *build the
datapath itself*.

**Prerequisites:** [Intro to C](../Intro_Func_Prog/Intro_C.ipynb);
[DSP Workshop 1](../Intro_DSP/README.md) for the filtering sessions.

---

## Workshop 1 — Introduction to FPGA *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — What is an FPGA?** | Theory | LUTs, flip-flops, routing fabric, DSP slices; FPGA vs CPU vs GPU trade-offs. |
| **S2 — HDL basics** | Application | Verilog/VHDL: modules, combinational vs sequential logic, simulate a counter. |
| **S3 — A hardware FIR filter** | Application | Implement the FIR filter from [DSP Filter Design](../Intro_DSP/README.md#workshop-2--filter-design-planned) in HDL; pipelining and fixed-point. |
| **S4 — Toolchain & deployment** | Application | Synthesis, place & route, timing closure; running on a real dev board. |

Contributions welcome — see the [contribution guide](../README.md#contributing).
