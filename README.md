# Auto AskReddit

> AI that automatically generates and posts realistic titles on askreddit

Fine tuned GPT-2 model generates realistic askreddit titles (app.py). After generating them, another program (auto_askreddit.py) automatically posts them using PRAW library.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```sh
pip3 install -r requirements.txt
```

if there is any error while installing from the requirements file, you can mannually install each dependency listed below.

```sh
praw
Flask
gpt-2-simple
tensorflow 1.x
```

## Usage example

The code consists of two files app.py and auto_askreddit.py

download the pretrained model from here https://drive.google.com/drive/folders/1ojZDnyCbau5fdJzE0DwyhOo1RS_hp7Fq?usp=sharing

There should be a "run2" folder within the "checkpoint" folder. Copy the whole thing (whole checkpoint filder and everything in it) and paste it in the same folder as the code files.

First run the app.py file to launch a flask server that generates the titles and returns them (GET).

```Python
python3 app.py
```

At this point, you can send request to the server using curl with query parameters.

nsamples : usually between 10 and 50 is fine. anymore than that means the server will take longer time.

batch_size : usually between 1 and 10.

temperature : strictly between 0 and 1

```sh
curl -v http://localhost:5000/generate/?nsamples=2&batch_size=1&temperature=0.9
```

But if you want to automatically post to reddit, you have to first get the client_id and client_secret.

Here is a great video on how to get those. https://www.youtube.com/watch?v=wAN8b38U_8c

After that, open the auto_askreddit.py file and type the client_id, client_secret, reddit username, reddit password and user agent name.

while the app.py is running, open a new terminal and run the auto_askreddit.py along with command line arguments to select the number of titles to generate, batch size and temperature(creativity).

```Python
python3 auto_askreddit.py -n 10 -b 1 -t 0.9
```

for each title that it recieved from the server, it will ask your permission to post it or not.
