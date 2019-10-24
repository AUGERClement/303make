#!/bin/bash
# prepare_my_repo.bash

blih -u clement.auger@epitech.eu repository create $1
blih -u clement.auger@epitech.eu repository setacl $1 ramassage-tek r
git clone git@git.epitech.eu:/clement.auger@epitech.eu/$1
