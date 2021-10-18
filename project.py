
my_login_dict = {"username": "PGR211","password": "Python"}

question1_dict = {
       1:{
      "question_text": "whats the largest city in Norway? Options: Bergen, Stavanger,Trondheim or Oslo? ",
      "correct answer" : "Oslo"},

       2:{
      "question_text": "What is the currency of Norway? Options: Euro, Pound, Krone or Deutsche Mark? ",
      "correct answer" : "Krone"},

      3:{
      "question_text": "What is the largest city in Norway? Options: Bergen, Stavanger,Trondheim or Oslo?",
      "correct answer" : "Oslo"},

      4:{
      "question_text": "When is constitution day (the national day) of Norway? Options: 27. May, 17. May, 17. April, 27. April?",
      "correct answer" : "17. May"},

      5:{
      "question_text": "What color is the background of the Norwegian flag? Options: Red, White, Blue, Yellow",
      "correct answer" : "Red"},

      6:{
      "question_text": "How many countries does Norway border? Options: 1, 2, 3, 4",
      "correct answer" : "3"},

      7:{
      "question_text": "What is the name of the university in Trondheim? Options: UiS, UiO, NMBU, NTNU",
      "correct answer" : "NTNU"},

      8:{
      "question_text": "How long is the border between Norway and Russia? Options: 96km, 196km, 296km, 396km",
      "correct answer" : "196km"},

      9:{
      "question_text": "Where in Norway is Stavanger? Options: North, South, South-west, South-east",
      "correct answer" : "South-west"},

      10:{
      "question_text": "From which Norwegian city did the world famous composer Edvard Grieg come? Options: Oslo, Bergen, Stavanger, Tromsø",
      "correct answer" : "Bergen"}
   }

class quiz:

    def __init__(self, questions_dict):
        self.questions_dict =  questions_dict

    def login(self, login_dict):
        Login_details = False

        while Login_details != True:

         if login_dict["username"] == "PGR211" and login_dict["password"] == "Python":

            Login_details = True
            print("You entered the correct details. The quiz will now begin.")

         else: 
            print("you entered the wrong username and/or password. Please try again.")

    def startQuiz(self):

        correctScore = 0
        wrong_score = 0
        answers_dict = { "wrong_questions": [],"wrong_answers": [], "corrected_answers": []}
        k = 0

        print("welcome to the quiz. This quiz has: " + str(len(self.questions_dict)) + " Questions. Let's start!")
        print(self.questions_dict[1]["question_text"])
        
        for questions in self.questions_dict:

             k=k+1
             print("Question number " + str(questions) + ":")
             answer = input(self.questions_dict[k]["question_text"])
             
             if answer == self.questions_dict[k]["correct answer"]:
                 correctScore = correctScore + 1
                
             else:
                wrong_score = wrong_score + 1
                answers_dict["wrong_answers"].append(answer)
                answers_dict["wrong_questions"].append(self.questions_dict[k]["question_text"])
                answers_dict["corrected_answers"].append(self.questions_dict[k]["correct answer"])

        print("You got " + str(correctScore) + " questions correct and " + str(wrong_score) + " wrong.")
        print("The questions you answered wrong are: " + str(answers_dict["wrong_questions"]) +
              " with the respective answers: " + str(answers_dict["wrong_answers"]) +
               " The correct answers are respectively: "  + str(answers_dict["corrected_answers"]))
   
def main():

    my_quiz = quiz(question1_dict)
    my_quiz.login(my_login_dict)
    my_quiz.startQuiz()

main()
    

