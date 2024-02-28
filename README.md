# alfred-transliterate
Alfred  Workflow for Transliteration

## Install
* Download .workflow file from [Releases](https://github.com/schwark/alfred-transliterate/releases)
* Can be installed from Packal at http://www.packal.org/workflow/transliterate-workflow
* Can also be downloaded from github as a zip file, unzip the downloaded zip, cd into the zip directory, and create a new zip with all the files in that folder, and then renamed to Smartthings.alfredworkflow
* Or you can use the workflow-build script in the folder, using
```
chmod +x workflow-build
./workflow-build . 
```

## Language

```
tl add <language>
```
This should only be needed once per install or after a reinit, or anytime you want to add a language to transliterate to

```
tl del <language>
```
This should only be needed anytime you want to remove a language to transliterate to

## Input Scheme

```
tl sch <input-scheme>
```
This should only be needed once per install or after a reinit, or anytime you want to change input scheme for transliteration to chinese like languages


## Transliteration

```
tl <message>
```
This is how to transliterate any message - result will be copied to the clipboard


## Reinitialize

```
tl reinit
```
This should only be needed if you ever want to start again for whatever reason - removes all API keys, devices, scenes, etc.

## Update

```
tl workflow:update
```
An update notification should show up when an update is available, but if not invoking this should update the workflow to latest version on github
