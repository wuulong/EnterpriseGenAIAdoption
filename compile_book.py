import os

files = [
    "ToC.md", "Chapter_1_1.md", "Chapter_1_2.md", "Chapter_1_3.md", "Chapter_1_4.md", "Chapter_1_5.md",
    "Chapter_2_1.md", "Chapter_2_2.md", "Chapter_2_3.md", "Chapter_2_4.md",
    "Chapter_3_1.md", "Chapter_3_2.md", "Chapter_3_3.md", "Chapter_3_4.md",
    "Chapter_4_1.md", "Chapter_4_2.md", "Chapter_4_3.md", "Chapter_4_4.md",
    "Chapter_5_1.md", "Chapter_5_2.md", "Chapter_5_3.md", "Chapter_5_4.md",
    "Chapter_6_1.md", "Chapter_6_2.md", "Chapter_6_3.md", "Chapter_6_4.md",
    "Appendix_A.md"
]

output_file = "Comprehensive_Enterprise_GenAI_Transformation.md"
cwd = "/Users/wuulong/github/bmad-pa/events/AIBooks/EnterpriseGenAIAdoption"

with open(os.path.join(cwd, output_file), "w", encoding="utf-8") as outfile:
    for i, filename in enumerate(files):
        filepath = os.path.join(cwd, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                if i < len(files) - 1:
                    outfile.write("\n\n---\n\n")
        else:
            print(f"Warning: {filename} not found.")

print(f"Successfully compiled {output_file}")
