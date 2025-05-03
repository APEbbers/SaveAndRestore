#!/bin/sh

# Variables
$WORKING_DIR
$FILE_NAME
$TARGET_DIR

# create a file in a directory (child-directory-a)
touch "${DIR_A}/${FILE_NAME}"
# move to the directory it is in
cd "${WORKING_DIR}"
# move the file to another directory (child-directory-b)
mv "${FILE_NAME}" "${TARGET_DIR}/"
# # move to that directory
# cd "${DIR_B}"
# # move the file to the parent directory
# mv "${FILE_NAME}" ../