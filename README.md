# ai-methodist
 AI-Methodist
Intelligent curriculum design and educational content generation powered by LLMs.


📘 Project Overview 
AI-Methodist is an automated tool designed to assist educators and instructional designers in creating structured, pedagogically sound lesson plans and learning materials. 

Generic AI is a tool, but methodologically-aware AI is a teacher.

Coming from a linguistics and professional language training background, I noticed a significant lack of depth in standard LLM outputs. This project is my solution: an implementation of Bloom’s Taxonomy and CEFR standards into the AI workflow, ensuring every response serves a clear pedagogical purpose.


✨ Key Features 
• Structured Lesson Planning: Generates full lesson cycles (Warm-up, Presentation, Practice, Production).
• Adaptive Content: Adjusts complexity based on target audience level (e.g., A1 to C2 for language learning).
• Methodological Frameworks: Uses specific pedagogical prompts to ensure high-quality educational outcomes.
• [WIP] Exercise Generation: Automatically creates quizzes and practice tasks from any input text.


🛠 Tech Stack 
• Language: Python 3.10+
• AI Models: OpenAI API (GPT-4 / GPT-3.5) / Gemini API
• Frameworks: LangChain (for prompt orchestration) 
• Data Handling: Pandas, JSON

📈 Project Roadmap 
• [x] Initial research and methodological framework design.
• [x] Core Python script for basic prompt generation.
• [ ] Integration with Telegram Bot / Streamlit Web UI.
• [ ] Support for multiple languages and subjects.
• [ ] PDF export for generated lesson plans.



📂 Structure 
ai-methodist/
├── src/
│   ├── generator.py       # Main logic for AI generation
│   ├── prompts.py         # My custom methodological prompt templates
│   └── utils.py           # Helper functions
├── data/                  # Sample inputs and outputs
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation


👩‍🔬 Linguistic Approach 
In this project, I apply my background in linguistics to:
1.  Optimize Prompt Engineering using semantic analysis.
2.  Ensure Scaffolding (building on prior knowledge) in AI-generated sequences.
3.  Control Lexical Density for different learner levels.


🚀 How to Run 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-methodist.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python src/generator.py
   ```

---

📚 🤝 Contact
Valery Pozdniakova – PhD in Linguistics / NLP Enthusiast
@valery_poz
