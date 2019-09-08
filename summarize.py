# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 10


def summarized(input):
    url = input
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    final_output = ''

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        for word in sentence.words:
            final_output = final_output + word + ' '
        final_output =  final_output[:-1] + '.\n\n'

    return final_output[:-2]