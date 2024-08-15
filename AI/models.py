from django.db import models

class TwoShotPrompt(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    input1 = models.TextField()
    output1 = models.TextField()
    input2 = models.TextField()
    output2 = models.TextField()

    def __str__(self):
        return f"{self.title} - ID: {self.id}"

    class Meta:
        verbose_name_plural = "Two-Shot Prompts"

    def get_prompt(self, myinput):
        prompt = f"""
        {self.instructions}

        INPUT: {self.input1}
        OUTPUT: {self.output1}

        INPUT: {self.input2}
        OUTPUT: {self.output2}

        INPUT: {myinput}
        OUTPUT:
        """
        return prompt.strip()