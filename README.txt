AI Study Assistant - fixed starter files

1. Put main.py, requirements.txt and your .env file in the same project folder.
2. Create a NEW Gemini API key. The key previously uploaded must be revoked.
3. Copy .env.example to a file named .env.
4. Replace the placeholder with your NEW key:
   GEMINI_API_KEY=your_new_key
   Do not add quotes around the key.
5. Open VS Code terminal in this folder and run:
   python -m pip install -r requirements.txt
6. Run:
   python main.py

If VS Code uses a different Python interpreter, select the interpreter where
you installed the packages: Ctrl+Shift+P > Python: Select Interpreter.

The .env file is secret. Do not upload it to GitHub or share it.
