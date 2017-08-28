# hackIIITD

**AI for social cause**

We have built a discussion forum using **Discourse** in which we analyze the user's post and comments that we run throug a trained **NLP (Artificial Intelligence)** model built using **NLTK** which gives us a score of the likeliness of the person having **depression** (<-0.8) and a tag which tells about the status of the likeliness of **anxiety**.

We have hosted our forum on **Digital Ocean** at http://techwalkers.tech.
It sends the data to our **Django api** which runs it through the **sentiment module** and gives us the depression score and anxiety tag.

Screenshots :

![b](https://user-images.githubusercontent.com/14929476/29761028-bf81926e-8be4-11e7-80cc-ce1770f4084a.png)

![a](https://user-images.githubusercontent.com/14929476/29761029-c42af940-8be4-11e7-91d9-1abb38d2b430.png)
