const express = require('express');
const axios = require('axios');
const { parseStringPromise } = require('xml2js');
const app = express();
const port = process.env.PORT || 3000;



const getMediumArticles = async () => {
    try {
        const url = 'https://medium.com/feed/@md.abir1203';
        const response = await axios.get(url);
        const feed = await parseStringPromise(response.data, { explicitArray: false });
        return feed.rss.channel.item;
    } catch(error) {
        console.error('Error while fetching Medium articles', error);
        return [];
    }
};



app.get('/', async (req, res) => {
    const articles = await getMediumArticles();
    const markdown = articles.map(article => {
      return `* [${article.title}](${article.link}) - ${article.pubDate}`;
    }).join('\n');
    res.send(markdown);
  });
  

app.listen(port, () => {
    console.log('Server running on http://localhost:${port}');
});
