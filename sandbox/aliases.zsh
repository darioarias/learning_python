#! /bin/bash

_args_exits() {
  # echo "arg $1"
  if [ -z $1 ]; then
    return -1
  else 
    return 0
  fi
}

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

create_commit_code() {
  if [ -z $1 ]; then
    echo "You must provide a file to create and add to git"
    return -1
  elif [ -z $2 ]; then
    echo "You did not provide a message for git commit"
    return -1
  fi
  
  echo $1 | xargs -I % sh -c "{ touch % && git add % && git commit -m '$2' && code $1 && nodemon $1; }"
  # echo "git commit -m '$2'"
  return $?
}

watch() {
  nodemon $1
  return $?
}