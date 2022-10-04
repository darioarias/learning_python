#! /bin/bash

create_code() {
  if [ -z $1 ]; then
    echo "You must provide a file to create and open"
    return -1
  fi
  echo "$1" | xargs -I % sh -c "{ touch % && code %; }"
}

create_add() {
  if [ -z $1 ]; then
    echo "You must provide a file to create and add to git"
    return -1
  fi
  
  echo $1 | xargs -I % sh -c "{ touch % && git add %; }"
  return $?
}

create_commit() {
  if [ -z $1 ]; then
    echo "You must provide a file to create and add to git"
    return -1
  elif [ -z $2 ]; then
    echo "You did not provide a message for git commit"
    return -1
  fi
  
  echo $1 | xargs -I % sh -c "{ touch % && git add % && git commit -m '$2'; }"
  return $?
}

new_commit_code() {
  COMMIT_MSG="$2"
  if [ -z $1 ]; then
    echo "You must provide a file to create and add to git">&2
    return -1
  elif [ -z $2 ]; then
    echo "You did not provide a message for git commit">&1
    COMMIT_MSG="Create $1"
  fi
  
  sh -c "{ touch $1 && git add $1 && git commit -m '$COMMIT_MSG' && code $1 && nodemon $1; }"
  return $?
}

add_commit() {
  COMMIT_MSG="$2"
  if [ -z $1 ]; then
    echo "You must provide a file to create and add to git">&1
    return -1
  elif [ -z $2 ]; then
    echo "You did not provide a message for git commit">&1
    COMMIT_MSG="update $1"
  fi 
  echo $1 | xargs -I % sh -c "{ git add % && git commit -m '$COMMIT_MSG'; }"
}

watch() {
  nodemon $1
  return $?
}