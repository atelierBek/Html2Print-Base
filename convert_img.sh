#!/bin/bash
ARTICLE=$1
FORMAT=$2
echo $ARTICLE

mkdir articles/$ARTICLE/img/bdef
mkdir articles/$ARTICLE/img/hdef
cp articles/$ARTICLE/img/*.$FORMAT articles/$ARTICLE/img/hdef/

convert articles/$ARTICLE/img/hdef/*.$FORMAT -resize 600x -set filename:base articles/$ARTICLE/img/bdef/"%[base]" "%[filename:base].$FORMAT"

echo "c'est bon !!!! "
