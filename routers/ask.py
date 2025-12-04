from fastapi import APIRouter
from services.embeddings import search
from services.llm import answer_questions
router = APIRouter()
@router.get("/")
def ask_question(question: str):
    docs = search(question)
    context = "\n\n".joins(docs)
    answer = answer_questions(question,context)
    return{"question": question,"context":context, "answer": answer}
