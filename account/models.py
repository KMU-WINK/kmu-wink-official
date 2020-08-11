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


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name="이메일")
    name = models.CharField(max_length=20, null=False, verbose_name="이름")
    student_number = models.IntegerField(unique=True, null=False, verbose_name="학번")
    department = models.CharField(max_length=20, null=False, verbose_name="학과")
    position = models.IntegerField(null=False, default=0, verbose_name="직책")
    join_date = models.DateTimeField(default=now, verbose_name="가입일")
    date_of_birth = models.DateField(null=False, verbose_name="생년월일")
    graduation_date = models.DateField(null=False, verbose_name="졸업(예정)일")
    payment = models.BooleanField(null=False, default=False, verbose_name="회비 납부 여부")
    profile_thumbnail = models.FilePathField(null=True, verbose_name="프로필 사진")
    description = models.CharField(max_length=300, null=True, verbose_name="자기소개")
    github_url = models.URLField(null=True, verbose_name="깃허브 주소")
    instagram_url = models.URLField(null=True, verbose_name="인스타그램 주소")
    website_url = models.URLField(null=True, verbose_name="웹 사이트 주소")
    is_active = models.BooleanField(default=True, verbose_name="회원 활성 여부")
    is_admin = models.BooleanField(default=False, verbose_name="관리자 여부")
    is_staff = models.BooleanField(default=False, verbose_name="간부 여부")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'name', 'student_number', 'department', 'position', 'graduation_date']
