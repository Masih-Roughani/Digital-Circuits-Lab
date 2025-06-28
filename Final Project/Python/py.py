from fpdf import FPDF

# واژه‌های روز پنجم (۱۰۱ تا ۱۲۵)
day5_words = [
    ("pipeline flush", "The process of clearing instructions from a pipeline, usually due to branch misprediction."),
    ("microcode", "Low-level instructions that implement higher-level machine instructions."),
    ("CPI (Cycles Per Instruction)", "Average number of clock cycles per instruction."),
    ("instruction latency", "Time taken for an instruction to pass through the pipeline."),
    ("hyper-threading", "Intel's technology to run two threads per core for parallelism."),
    ("multicore processor", "A CPU with multiple cores that can execute instructions independently."),
    ("NUMA (Non-Uniform Memory Access)",
     "A memory design where access time depends on the memory location relative to the processor."),
    ("SIMD", "Single Instruction, Multiple Data – executes the same instruction on multiple data."),
    ("MIMD", "Multiple Instruction, Multiple Data – different instructions on different data."),
    ("instruction scheduler", "Decides the order of instruction execution."),
    ("instruction window", "Set of instructions considered for execution at one time."),
    ("write-back", "Final stage where computed result is written to register."),
    ("data hazard", "A pipeline hazard from data dependencies between instructions."),
    ("control signal", "Signals that control operation of CPU components."),
    ("data forwarding", "Technique to pass data directly from one pipeline stage to another."),
    ("memory bottleneck", "A condition where memory speed limits CPU performance."),
    ("execution unit", "A part of the CPU that performs operations like arithmetic or logic."),
    ("hardware thread", "An independently scheduled thread on a processor core."),
    ("task-level parallelism", "Running different tasks simultaneously."),
    ("fine-grained parallelism", "Parallelism at the level of individual instructions."),
    ("coarse-grained parallelism", "Parallelism at the level of functions or threads."),
    ("bus latency", "Delay associated with data transfer over a bus."),
    ("clock skew", "Timing difference between different parts of a digital circuit."),
    ("load-use hazard", "A data hazard caused when an instruction uses data not yet available."),
    ("reservation station", "Holds instructions waiting for operands in out-of-order execution.")
]

# شماره‌گذاری از ۱۰۱
day5_flashcards = [(i + 101, word, definition) for i, (word, definition) in enumerate(day5_words)]

# ساخت فایل PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

for number, word, definition in day5_flashcards:
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"{number}. {word}", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"{definition}\n")

# خروجی فایل
pdf.output("Computer_Engineering_Flashcards_Day5.pdf")
print("✅ فایل PDF ساخته شد: Computer_Engineering_Flashcards_Day5.pdf")
