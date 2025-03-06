# Sentiment Analysis - YouTube Comments
### Analyzing the Impact of Social Media Influencers on Trust Building
A Text Mining Approach: Sentiment Analysis and Topic Modelling

## Background
Social media platform such as YouTube have transformed the way that people interact, share information, and build trust. Influencer like Mr. Beast, known for his large-scale challenge and generous giveaways, play a vital role in shaping consumer behavior and trust within digital environments. Although the growing influence of social media personalities, there is limited research on how these influencers, especially highly popular ones like Mr. Beast, build trust with their audiences.

## Aims
This dissertation aims to investigate the strategies of how Mr. Beast build trust with his audience on YouTube. The research focuses on understanding how his content, including high-stakes challenges and charitable deeds, affects audience engagement and trust-building.

## Methods
The study utilised text mining and data mining techniques to analyse comments from Mr. Beast top 10 most viewed YouTube videos. A total 10,000 comments were analysed by using sentiment analysis, topic modelling, and word frequency analysis to identify patterns and topics related to trust-building.

## Results
The analysis revealed that Mr. Beast’s consistent high-quality content, profession and neutral comments, and philanthropic efforts significantly contribute to building test with his audience. The sentiment analysis indicated highly positive interactions, while topic modelling highlighted the topics of generosity, excitement, and loyalty.

### Exploratory Data
Table 1 provides a summary of these columns, exhibiting the total views, total reply counts, and total like counts for each video. Additionally, the titles of the videos were included in the table which offers a clearer insight into the content that drives audience engagement. The table is ordered by view count, with the video titled "$456,000 Squid Game In Real Life!" leading with over 642 million views, highlighting its broad appeal. Other videos, such as "Last To Leave Circle Wins $500,000" and "$1 vs $500,000 Plane Ticket!", also garnered significant viewership, with over 462 million and 409 million views, respectively. 

<table align="center">
  <thead>
    <tr>
      <th>Rank</th>
      <th>Video ID</th>
      <th>Video Title</th>
      <th>Total View</th>
      <th>Total Reply Count</th>
      <th>Like Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="right">1</td>
      <td align="left">0e3GPea1Tyg</td>
      <td align="left">$456,000 Squid Game In Real Life!</td>
      <td align="right">642,694,545</td>
      <td align="right">17,864</td>
      <td align="right">1,319,017</td>
    </tr>
    <tr>
      <td align="right">2</td>
      <td align="left">zxYjTTXc-J8</td>
      <td align="left">Last To Leave Circle Wins $500,000</td>
      <td align="right">462,329,949</td>
      <td align="right">11,726</td>
      <td align="right">464,176</td>
    </tr>
    <tr>
      <td align="right">3</td>
      <td align="left">1WEAJ-DFkHE</td>
      <td align="left">$1 vs $500,000 Plane Ticket!</td>
      <td align="right">409,311,013</td>
      <td align="right">2,210</td>
      <td align="right">181,055</td>
    </tr>
    <tr>
      <td align="right">4</td>
      <td align="left">FM7Z-Xq8Drc</td>
      <td align="left">Ages 1 - 100 Fight For $500,000</td>
      <td align="right">383,854,152</td>
      <td align="right">6,561</td>
      <td align="right">794,931</td>
    </tr>
    <tr>
      <td align="right">5</td>
      <td align="left">iogcY_4xGjo</td>
      <td align="left">$1 vs $1,000,000 Hotel Room!</td>
      <td align="right">361,436,203</td>
      <td align="right">9,142</td>
      <td align="right">351,888</td>
    </tr>
    <tr>
      <td align="right">6</td>
      <td align="left">48h57PspBec</td>
      <td align="left">$1 vs $1,000,000,000 Yacht!</td>
      <td align="right">359,754,283</td>
      <td align="right">7,136</td>
      <td align="right">260,809</td>
    </tr>
    <tr>
      <td align="right">7</td>
      <td align="left">9bqk6ZUsKyA</td>
      <td align="left">I Spent 50 Hours Buried Alive</td>
      <td align="right">323,517,354</td>
      <td align="right">17,064</td>
      <td align="right">711,370</td>
    </tr>
    <tr>
      <td align="right">8</td>
      <td align="left">fMfipiV_17o</td>
      <td align="left">I Spent 50 Hours In Solitary Confinement</td>
      <td align="right">322,849,307</td>
      <td align="right">1,852</td>
      <td align="right">167,583</td>
    </tr>
    <tr>
      <td align="right">9</td>
      <td align="left">r7zJ8srwwjk</td>
      <td align="left">Would You Sit In Snakes For $10,000?</td>
      <td align="right">320,466,735</td>
      <td align="right">14,399</td>
      <td align="right">596,675</td>
    </tr>
    <tr>
      <td align="right">10</td>
      <td align="left">GLoeAJUcz38</td>
      <td align="left">Press This Button To Win $100,000!</td>
      <td align="right">317,508,296</td>
      <td align="right">6,791</td>
      <td align="right">288,911</td>
    </tr>
  </tbody>
</table>

<p align="center"><b><i>Table 1: Video Title, Total View, Total Reply, Like Count of each video</b></i></p>

</br>
Figure 1 shows that the video “$456,000 Squid Game In Real Life! “ leads with over 1.7 thousands of replies which reflects active viewer participation. Notably,  “Ages 1 – 100 Fight For $500,000”, “I Spent 50 Hours Buried Alive”, and “Would You Sit In Snakes For $10,000? “ having the total reply count over 10000. “$456,000 Squid Game In Real Life!”, “Ages 1 – 100 Fight For $500,000”, “I Spent 50 Hours Buried Alive”, and “Would You Sit In Snakes For $10,000?” each had over 10,000 replies, highlighting their potential for attracting an huge audience response. 
</br>
<p align="center">
  <img width="718" alt="Total reply count" src="https://github.com/user-attachments/assets/9ca8606b-e20a-42a9-8e0f-873f895597d6">
</p>
<p align="center"><b><i>Figure 1: Total reply count of each video</b></i></p>

</br>
As shown in figure 2 the video “$456,000 Squid Game In Real Life!” is particularly noteworthy, having accumulated over 1.3 million likes This reflects a significant positive reception from the audience. Similarly, video such as Ages 1 – 100 Fight For $500,000”, “ I Spent 50 Hours Buried Alive”, and “ Would You Sit In Snakes For $10,000?” also received a huge number of likes, with 794,931, 711,370, and 596,675 respectively.
</br>
<p align="center">
  <img width="704" alt="Total comment like count" src="https://github.com/user-attachments/assets/4f1b231e-cb33-4191-90a9-0a43d613c2b5">
</p>
<p align="center"><b><i>Figure 2: Total comment like count of each video</b></i></p>

### N-Gram
Next step was to identify the most frequently used two-words and three-words phrases through all comments in each video, in order to show the most common and significant word combinations in the content. The results are illustrated in Figure 3, 4, 5 and 6 and were discussed below.
Figures 3 and 4 show that "mr beast" and "10 000" are the top two most frequently used word combination in both comment’s dataset and Mr. Beast comment’s dataset. In the comment data, "mr beast" is the most significant used two word with the count of 1,011, followed by "10 00" with 86 occurrences. the first, with 1011 count, and "10 000" the second, with 86 counts, in comments’ data and “10 000” the first, with 45 counts, and "mr beast" the second, with 29 counts in Mr. Beast’s data. In contrast, in Mr. Beast’s dataset, "10 000" is the most frequent two words, with 45 times, while "mr beast" comes second with 29 times. 

<p align="center">
  <img width="896" alt="Comment’s Bigram" src="https://github.com/user-attachments/assets/bb062c11-6247-4fb3-bc9e-ca9317d8d0c3">
</p>
<p align="center"><b><i>Figure 3: Comment’s Bigram</b></i></p>
<p align="center">
  <img width="949" alt="Mr. Beast’s Bigram" src="https://github.com/user-attachments/assets/c347ccdd-a8ca-408b-8dc1-34ddd5ad9263">
</p>
<p align="center"><b><i>Figure 4: Mr. Beast’s Bigram</b></i></p>

</br>
Trigram, a combination of three words, was revealed in Figure 5, Comment’s data, and Figure 6, Mr. Beast replies. In audience comments, "love mr beast" and "appreciate much effort" are the top two most frequently used trigram, sharing the same number 43 times. Conversely, in Mr. Beast’s replies, "half million dollars" and "rock paper scissors" were the most common three words, with 16 and 8 times in the whole data. Last, a word cloud is created based on the word frequency and has provide a slightly more understandable and elegant, making it easier to visualise the data (Figure 7 & 8). 
<p></p>
<p align="center">
  <img width="906" alt="Comment’s Trigram" src="https://github.com/user-attachments/assets/584bd66d-516b-42a3-b5a8-2c244f1bd261">
</p>
<p align="center"><b><i>Figure 5: Comment’s Trigram</b></i></p>
<p align="center">
  <img width="1013" alt="Mr. Beast’s Trigram" src="https://github.com/user-attachments/assets/ec1e920b-e1b0-45bc-bda7-cc3655d80580">
</p>
<p align="center"><b><i>Figure 6: Mr. Beast’s Trigram</b></i></p>
<p align="center">
  <img width="683" alt="Comment’s Word Cloud" src="https://github.com/user-attachments/assets/9040c213-2e3e-4bd3-a1dc-a99545066c06">
</p>
<p align="center"><b><i>Figure 7: Comment’s Word Cloud</b></i></p>
<p align="center">
  <img width="674" alt="Mr. Beast’s Word Cloud" src="https://github.com/user-attachments/assets/7573b122-c4c4-472f-bbae-49c02039f0b6">
</p>
<p align="center"><b><i>Figure 8: Mr. Beast’s Word Cloud</b></i></p>

### Sentiment Analysis
The results of the Sentiment analysis of both the audience’s comments and Mr. Beast’s comments and replies are presented in Figure 9.  In the audience’s comment, it is noticeable that the positive and neutral sentiments are the majority sentiment in the dataset, with 44.7% and 42.5% of the dataset, respectively. On the other hand, Mr. Beast’s comments show a different pattern, neutral sentiment is the most prevalent, with 61% of the dataset, followed by positive sentiment at 25.8%, while negative sentiment remains minimal at only 13.2%.
<p></p>
<p align="center">
  <img width="993" alt="image" src="https://github.com/user-attachments/assets/0aaac501-d474-4db4-ba94-2a3029691543">
</p>
<p align="center"><b><i>Figure 8: Pei chart of the sentiment percentage in Comment’s Data and Mr. Beast’s replies</b></i></p>

### Topic Modelling
The topics of audience’s comments and Mr. Beast replies and comments that generated by the BERTopic model are provided in Table 2 and 3. Each of the topic reflected common themes and subjects discussed in the comments and Mr. Beast’s replies. In BERTopic, topic -1, represents the all the outliers that should typically be ignored and won’t be discussed. The first topic (Topic 0) of the audience’s comments can be related to appreciation to Mr. Beast’s early video, terms like, "early", "videos", "love", "appreciate", etc. The second topic (Topic 1) is more strongly associate with Mr. Beast’s video, particularly those involves games and giveaways, words like, "squid", "games", "give", etc. The third topic (Topic 2) highlights discussion around Mr. Beast team members, such as, "Chandler", "Karl", "Chris", and "Davidson". Finaly, the fourth topic (Topic 3) is about the luxury and wealth, indicated by terms like, "money", "yacht", "boat", "hotel", etc. In contrast, the first topic of Mr. Beast’s words is about the interaction with his team, terms like, "Karl", "Chris", "right", "gonna", etc. The second topic is related to a large amount of money, such as "10", "000", "million", "money", and "dollars". The third topic is associated with energetic and dynamic atmosphere. Last, fourth topic revolved around food-related discussion, including words like "feastables", "chocolate", "food", and "pizza".

<table align="center">
  <thead>
    <tr>
      <th>Topic</th>
      <th>Word 1</th>
      <th>Word 2</th>
      <th>Word 3</th>
      <th>Word 4</th>
      <th>Word 5</th>
      <th>Word 6</th>
      <th>Word 7</th>
      <th>Word 8</th>
      <th>Word 9</th>
      <th>Word 10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="right">Topic -1</td>
      <td align="left">beast</td>
      <td align="left">mr</td>
      <td align="left">jimmy</td>
      <td align="left">money</td>
      <td align="left">guy</td>
      <td align="left">man</td>
      <td align="left">would</td>
      <td align="left">videos</td>
      <td align="left">one</td>
      <td align="left">win</td>
    </tr>
    <tr>
      <td align="right">Topic 0</td>
      <td align="left">jimmy</td>
      <td align="left">early</td>
      <td align="left">first</td>
      <td align="left">videos</td>
      <td align="left">one</td>
      <td align="left">love</td>
      <td align="left">views</td>
      <td align="left">10</td>
      <td align="left">appreciate</td>
      <td align="left">best</td>
    </tr>
    <tr>
      <td align="right">Topic 1</td>
      <td align="left">beast</td>
      <td align="left">mr</td>
      <td align="left">mrbeast</td>
      <td align="left">please</td>
      <td align="left">love</td>
      <td align="left">squid</td>
      <td align="left">best</td>
      <td align="left">videos</td>
      <td align="left">game</td>
      <td align="left">give</td>
    </tr>
    <tr>
      <td align="right">Topic 2</td>
      <td align="left">chandler</td>
      <td align="left">karl</td>
      <td align="left">pete</td>
      <td align="left">chris</td>
      <td align="left">davidson</td>
      <td align="left">tom</td>
      <td align="left">brady</td>
      <td align="left">nolan</td>
      <td align="left">pickles</td>
      <td align="left">carl</td>
    </tr>
    <tr>
      <td align="right">Topic 3</td>
      <td align="left">money</td>
      <td align="left">yacht</td>
      <td align="left">boat</td>
      <td align="left">ship</td>
      <td align="left">dollar</td>
      <td align="left">cruise</td>
      <td align="left">hotel</td>
      <td align="left">much</td>
      <td align="left">flag</td>
      <td align="left">room</td>
    </tr>
  </tbody>
</table>
<p align="center"><b><i>Table 6: Comment’s topic words</i></b></p>

<table align="center">
  <thead>
    <tr>
      <th>Topic</th>
      <th>Word 1</th>
      <th>Word 2</th>
      <th>Word 3</th>
      <th>Word 4</th>
      <th>Word 5</th>
      <th>Word 6</th>
      <th>Word 7</th>
      <th>Word 8</th>
      <th>Word 9</th>
      <th>Word 10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="right">Topic -1</td>
      <td align="left">one</td>
      <td align="left">got</td>
      <td align="left">go</td>
      <td align="left">let</td>
      <td align="left">next</td>
      <td align="left">like</td>
      <td align="left">oh</td>
      <td align="left">right</td>
      <td align="left">even</td>
      <td align="left">ship</td>
    </tr>
    <tr>
      <td align="right">Topic 0</td>
      <td align="left">right</td>
      <td align="left">gonna</td>
      <td align="left">oh</td>
      <td align="left">chris</td>
      <td align="left">jimmy</td>
      <td align="left">karl</td>
      <td align="left">one</td>
      <td align="left">go</td>
      <td align="left">hey</td>
      <td align="left">get</td>
    </tr>
    <tr>
      <td align="right">Topic 1</td>
      <td align="left">000</td>
      <td align="left">million</td>
      <td align="left">10</td>
      <td align="left">plane</td>
      <td align="left">dollars</td>
      <td align="left">yacht</td>
      <td align="left">money</td>
      <td align="left">boat</td>
      <td align="left">grand</td>
      <td align="left">half</td>
    </tr>
    <tr>
      <td align="right">Topic 2</td>
      <td align="left">music</td>
      <td align="left">upbeat</td>
      <td align="left">cheering</td>
      <td align="left">explosion</td>
      <td align="left">contestants</td>
      <td align="left">booming</td>
      <td align="left">laughing</td>
      <td align="left">dinging</td>
      <td align="left">bell</td>
      <td align="left">speakers</td>
    </tr>
    <tr>
      <td align="right">Topic 3</td>
      <td align="left">feastables</td>
      <td align="left">chocolate</td>
      <td align="left">food</td>
      <td align="left">pizza</td>
      <td align="left">dinner</td>
      <td align="left">eat</td>
      <td align="left">bars</td>
      <td align="left">pie</td>
      <td align="left">steak</td>
      <td align="left">meal</td>
    </tr>
  </tbody>
</table>
<p align="center"><b><i>Table 7: Mr. Beast’s comments and replies topic words</i></b></p>

</br>
Figure 9 shows the distribution of sentiment labels across different topics by combining the results of Sentiment Analysis and Topic Modelling. The y-axis represents the number of the comments, and the x-axis shows the corresponding topics. In the audience’s comments, positive sentiment is the most frequent in the top three topics, accounting for 45%, 55% and 44%. This is followed by neutral sentiment with 41%, 36%, and 41%, respectively. Negative is the least prevalent across these topics. The pattern in Mr. Beast’s comments and replies is slightly different from the audience’s comments. It shows that neutral sentiment the most prominent, making up 60.6%, 62.6%, and 46.7% of the top three topics. Positive sentiment follows, with 24.7%, 28.5%, and 34.8%, while negative sentiment remains the least common, consistent with the audience's comments. 
<p></p>
<p align="center">
  <img width="991" alt="image" src="https://github.com/user-attachments/assets/70c9d7d8-ef95-4341-b190-ed0a3fbcea57">
</p>
<p align="center"><b><i>Figure 9: Comment VADER Sentiment Labels by Topic with Percentages</b></i></p>


## Conclusions
Mr Beast’s method of making content combines entertainment with giving back to the community and has proven effective in building a connection with his audience members who trust and support. This research provides insights on how trusts developed in the modern digital era and valuable implications for influencers and marketers aiming to improve their relationships, with followers through various online platforms.


