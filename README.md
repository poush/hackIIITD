# hackIIITD

**AI for social cause**

We have built a discussion forum using **Discourse** in which we analyze the user's post and comments that we run throug a trained **NLP (Artificial Intelligenct)** model built using **NLTK** which gives us a score of the likeliness of the person having **depression** (<-0.8) and a tag which tells about the status of the likeliness of **anxiety**.

We have hosted our forum on **Digital Ocean** at http://techwalkers.tech.
It sends the data to our **Django api** which runs it through the **sentiment module** and gives us the depression score and anxiety tag.
