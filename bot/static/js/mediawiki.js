// Function for search with API MediaWiki
function mediawikiSearchCallback(response) {
    const pageIdList = response['query']['geosearch'];
    pageId = pageIdList[0]['pageid'];
    // Number of the searched page
    for (let i = 0; i < pageIdList.length; i++) {
        if (pageIdList[i]['title'] === geoLocation['route']) {
            pageId = pageIdList[i]['pageid'];
        }
    }
    console.log('[MEDIAWIKI] PAGE_ID : ' + pageId);

    backEnd['dataPageId']['pageids'] = pageId;
    mediaWikiObject.ajax(backEnd['dataPageId'], mediawikiPageidCallback);
}


// Function for displaying the response of the MediaWiki API
function mediawikiPageidCallback(response) {
    const lien = 'https://fr.wikipedia.org/wiki?curid=' + pageId;
    const result = response['query']['pages'][0]['extract'];
    console.log('[MEDIAWIKI] extract : ' + result);
    if (result.length !== 0) {
        msgBot = backEnd['answers'][1] + result;
    } else {
        msgBot = backEnd['answers'][1] +
            "Bon, j'ai un soucis pour récupérer les informations mais vous pouvez les trouver à cette page ";
    }
    console.log('[MEDIAWIKI] ANSWER_BOT : ' + msgBot);

    chatBot.send(msgBot + ' [<a href="' + lien + '">En savoir plus sur Wikipedia</a>]');
}