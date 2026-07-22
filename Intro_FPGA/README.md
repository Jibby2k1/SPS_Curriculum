# Introduction to FPGA Systems

Application track: pushing signal processing into hardware. Where
[GPU workshops](../Intro_GPU/README.md) parallelize software, FPGAs let you *build the
datapath itself*.

**Prerequisites:** [Intro to C](../Intro_Programming/Intro_C.ipynb);
[DSP Workshop 1](../Intro_DSP/README.md) for the filtering sessions.

---

## Workshop 1 — Introduction to FPGA *(draft — pending review)*

Material: [`Intro_FPGA.ipynb`](./Intro_FPGA.ipynb) — Verilog must be simulated (Icarus/EDA Playground); carries a review banner.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — What Is an FPGA?** | Theory | §2: LUTs/FFs/DSP slices; time vs space computing; the CPU/GPU/FPGA trade table | Know when the FPGA wins and why. |
| **S2 — HDL Basics** | Application | §3: combinational vs sequential Verilog, a counter + testbench + waveforms | Describe circuits, don't instruct; simulate and read waveforms. |
| **S3 — A Hardware FIR Filter** | Application | §4: transposed FIR in Q1.15 from [Filter Design](../Intro_DSP/README.md#workshop-2--filter-design-available) taps | Fixed-point, pipelining, golden-model verification. |
| **S4 — Toolchain & Deployment** | Application | §5: synthesis → place & route → timing closure → bitstream | Understand slack; blink a real board. |

## Workshop 2 — HLS for FPGA: C to Gates *(draft — pending review)*

Material: [`HLS_for_FPGA.ipynb`](./HLS_for_FPGA.ipynb) — needs Vitis HLS; carries a review banner

| Session | Objectives |
|---|---|
| **S1 — C With Hardware Semantics** | ap_fixed, pragmas, the II=1 FIR; the report as the real output. |
| **S2 — Interfaces & Integration** | AXI-Stream/Lite; the C testbench as golden model. |

Contributions welcome — see the [contribution guide](../README.md#contributing).
