from .page86 import page86_ai_msg

def sub():
    print("메인에서 실행하는 서브함수")

def main() -> None:
    # print("메인화면 : app.py")
    # sub()

    page86_ai_msg()

    # page95.py
    from . import page95
    # 함수 없을 시 문서 전체 실행(import만 해도 실행 가능)

    # page99.py
    from . import page99

    # page101.py Langgraph
    from . import page101
