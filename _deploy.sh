docker buildx build --platform linux/amd64 -t code-comment-prediction .

docker tag code-comment-prediction registry.heroku.com/code-comment-prediction/web

docker push registry.heroku.com/code-comment-prediction/web

heroku container:release web -a code-comment-prediction
