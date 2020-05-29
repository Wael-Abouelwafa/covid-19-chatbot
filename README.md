Chat Bot

the Covid-19 chat bot runs in the local host, it’s still a little bit need more training, so we implement about 100 Q& A as a training set in .TXT file ,but that’s an early version, most probably we will be working on it’s performance ASAP, we are using from chatterbot ,Flask and ChatterBot Corpus Trainer for normal english wich is not powerful as Spacy but it works .
Installation

to use the Covid-19 chat bot follow these steps

    in Linux create a virtual env and activate it

$python -m venv venv
$source venv/bin/activate

    then colon the project in your folder using

git clone https://github.com/Wael-Abouelwafa/covid-19-chatbot.git

    install all the requirements

$pip install -r requirements.txt

Now you are ready to go !

    start the app from app.py

$python app.py

you will find a message ending with the url like so

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Jump into the link and you will directed to the landing page
covid-19 chatbot
