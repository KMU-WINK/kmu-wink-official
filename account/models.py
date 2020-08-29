from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.utils.timezone import now

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, date_of_birth, name, student_number, department, position, graduation_date):
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            name=name,
            student_number=student_number,
            department=department,
            position=position,
            graduation_date=graduation_date
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, date_of_birth, name, student_number, department, position, graduation_date):
        print(email, password, date_of_birth, name, student_number, department, position, graduation_date);
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            date_of_birth=date_of_birth,
            name=name,
            student_number=student_number,
            department=department,
            position=position,
            graduation_date=graduation_date
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

POSITION_CHOICE = [
    (20, '지도 교수'),
    (12, '이전 회장'),
    (11, '이전 부회장'),
    (10, '이전 간부'),
    (9, '회장'),
    (8, '부회장'),
    (7, '서기'),
    (6, '총무 부장'),
    (5, '운영 부장'),
    (4, '기획 부장'),
    (6, '총무 차장'),
    (3, '운영 차장'),
    (2, '기획 차장'),
    (1, '부원'),
    (0, '회원'),
]


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name="이메일")
    name = models.CharField(max_length=20, null=False, verbose_name="이름")
    student_number = models.IntegerField(unique=True, null=False, verbose_name="학번")
    department = models.CharField(max_length=20, null=False, verbose_name="학과", default="software")
    position = models.IntegerField(null=False, default=0, choices=POSITION_CHOICE, verbose_name="직책")
    prev_position = models.CharField(max_length=30, null=True, blank=True, verbose_name="이전 직책")
    join_date = models.DateTimeField(default=now, verbose_name="가입일")
    date_of_birth = models.DateField(null=False, verbose_name="생년월일")
    graduation_date = models.DateField(null=False, verbose_name="졸업(예정)일")
    payment = models.BooleanField(null=False, default=False, verbose_name="회비 납부 여부")
    profile_thumbnail = models.ImageField(null=False, default="static/assets/logo/wink-color.png", upload_to="static/images/upload/", verbose_name="프로필 사진")
    description = models.CharField(max_length=300, null=True, verbose_name="자기소개")
    github_url = models.URLField(null=True, blank=True, verbose_name="깃허브 주소")
    instagram_url = models.URLField(null=True, blank=True, verbose_name="인스타그램 주소")
    website_url = models.URLField(null=True, blank=True, verbose_name="웹 사이트 주소")
    is_active = models.BooleanField(default=True, verbose_name="회원 활성 여부")
    is_admin = models.BooleanField(default=False, verbose_name="관리자 여부")
    is_staff = models.BooleanField(default=False, verbose_name="간부 여부")


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'name', 'student_number', 'department', 'position', 'graduation_date']

    def __str__(self):
        return str(self.student_number) + ' ' + str(self.name)
    class Meta:
        verbose_name_plural = "회원"


class Emoji(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='related_user', verbose_name="공감 대상")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='related_owner', verbose_name="공감 소유자")
    content = models.CharField(max_length=100, null=False, verbose_name="공감 내용(이모티콘)")
    date = models.DateTimeField(default=now, verbose_name="공감 일")

    def __str__(self):
        return str(self.user.name) + '에게 ' + str(self.owner.name) + '이 남긴 이모티콘'
    class Meta:
        verbose_name_plural = "공감"