from django.db import models
from core.models import TimeStamped
from ckeditor_uploader.fields import RichTextUploadingField
from userapp.models import User


class QnaBoard(TimeStamped):
    """QnaBoard Model Definition"""

    TYPE_CHOICES = (
        ("A.일반", "A.일반"),
        ("B.유형1", "B.유형1"),
        ("C.유형2", "C.유형2"),
        ("D.유형3", "D.유형3"),
    )

    title = models.CharField("제목", max_length=200, null=False)
    type = models.CharField(
        "유형", choices=TYPE_CHOICES, null=False, max_length=20, default="일반"
    )
    content = RichTextUploadingField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "자주묻는 질문 관리"

    def __str__(self):
        return f"{self.title}"


class DirectQuestion(TimeStamped):
    """DirectQuestion Model Definition"""

    class Meta:
        verbose_name_plural = "1:1 문의"

    title = models.CharField("제목", max_length=300)
    content = models.TextField("내용", null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자", related_name="author"
    )
    is_complete = models.BooleanField("처리완료", default=False)
    answer = models.TextField("답변", null=True, blank=True)
    answer_file = models.FileField(
        "답변 보조자료",
        upload_to="question/",
        help_text="질문 응답에 필요한 첨부파일 입니다.",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} - {self.author.name}"


class OrderBoard(TimeStamped):
    """OrderBoard Model Definition"""

    class Meta:
        verbose_name_plural = "주문의뢰 관리"

    PRO_CHOICE = (
        ("패키지", "패키지"),
        ("쇼핑백", "쇼핑백"),
        ("형택", "형택"),
        ("기타제작물", "기타제작물"),
    )

    PRINT_SPEC = (
        ("없음", "없음"),
        ("4도 컬러인쇄", "4도 컬러인쇄"),
        ("1도 단색인쇄", "1도 단색인쇄"),
        ("별색인쇄", "별색인쇄"),
        ("UV인쇄", "UV인쇄"),
        ("기타인쇄", "기타인쇄"),
    )

    COATINGS = (
        ("없음", "없음"),
        ("무광라미네이팅", "무광라미네이팅"),
        ("유광라미네이팅", "유광라미네이팅"),
    )

    DESIGNS = (
        ("없음", "없음"),
        ("의뢰", "의뢰"),
    )

    PAPER_TYPE = (
        ("아트지", "아트지"),
        ("스노우화이트", "스노우화이트"),
        ("SC마니라", "SC마니라"),
        ("로얄아이보리", "로얄아이보리"),
        ("기타재질", "기타재질"),
    )

    title = models.CharField("제작의뢰명", max_length=200, null=False)
    company = models.CharField("상 호", max_length=100, null=False)
    name = models.CharField("성 명", max_length=20, null=False)
    password = models.CharField(
        "비밀번호", max_length=4, null=False, help_text="비밀번호는 의뢰 삭제 시 필요합니다."
    )
    tel = models.CharField("연락처", max_length=20, null=False)
    email = models.EmailField("이메일", null=False)

    pro_type = models.CharField(
        "제작물", choices=PRO_CHOICE, max_length=20, null=False, default="패키지"
    )
    pro_qny = models.IntegerField("제작수량", null=False)

    size_width = models.IntegerField("사이즈 가로(mm)", null=False)  # 가로
    size_length = models.IntegerField("사이즈 세로(mm)", null=False)  # 세로
    size_height = models.IntegerField("사이즈 높이(mm)", null=False)  # 높이

    design_yn = models.CharField(
        "디자인 유/무", max_length=30, null=False, choices=DESIGNS, default="없음"
    )
    paper_type = models.CharField(
        "종이재질", max_length=50, null=False, choices=PAPER_TYPE, default="아트지"
    )
    print_spec = models.CharField(
        "인쇄사양", max_length=30, null=False, choices=PRINT_SPEC, default="없음"
    )
    coating = models.CharField(
        "코 팅", max_length=30, null=False, choices=COATINGS, default="없음"
    )
    processing = models.CharField("후가공", max_length=50, null=False)

    content = models.TextField("문의내용", null=False)

    is_completed = models.BooleanField(
        "처리현황", default=False, help_text="처리가 완료 된 주문은 꼭 체크 해주세요."
    )

    file_1 = models.FileField("첨부파일1", upload_to="order/", null=True, blank=True)
    file_2 = models.FileField("첨부파일2", upload_to="order/", null=True, blank=True)
    file_3 = models.FileField("첨부파일3", upload_to="order/", null=True, blank=True)
