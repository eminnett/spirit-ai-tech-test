FROM python:3.7-alpine

WORKDIR /spirit_ai_tech_test

COPY . /spirit_ai_tech_test

ENV BUILD_PACKAGES bash curl-dev ruby-dev ruby-rdoc build-base
ENV RUBY_PACKAGES ruby ruby-io-console ruby-bundler
RUN apk update && \
    apk upgrade && \
    apk add $BUILD_PACKAGES && \
    apk add $RUBY_PACKAGES && \
    rm -rf /var/cache/apk/*

WORKDIR /spirit_ai_tech_test/roman_numeral_calculator

RUN gem update bundler
RUN bundle install

WORKDIR /spirit_ai_tech_test/web_api

RUN pip install pipenv
RUN pipenv install

EXPOSE 5000

CMD ["pipenv", "run", "python", "web_api.py"]