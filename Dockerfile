FROM ruby:3-bookworm

ENV GEM_HOME /gems
ENV PATH $GEM_HOME/bin:$PATH

RUN gem install jekyll bundler

VOLUME [ "/app" ]
WORKDIR /app

COPY Gemfile* ./
COPY *.gemspec ./

RUN bundle install
