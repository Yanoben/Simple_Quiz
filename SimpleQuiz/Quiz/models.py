from django.db import models


class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True, verbose_name='option1')
    op2 = models.CharField(max_length=200, null=True, verbose_name='option2')
    op3 = models.CharField(max_length=200, null=True, verbose_name='option3')
    op4 = models.CharField(max_length=200, null=True, verbose_name='option4')
    ans = models.CharField(max_length=200, null=True,
                           verbose_name='Answer(choose op number)')

    def __str__(self):
        return self.question
