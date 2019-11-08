---
title: 'Sound Classification Assignment'
disqus: hackmd
---

Sound Classification
===

## Table of Contents

[TOC]

## Introduction

In this project, there are five different sounds that are classified, Microwave, Vacuum, Blender, Music, and an Alarm. Twenty, 30 second samples were recorded of each sound, totaling 100 different samples. A machine learning model is trained using the sound to classify the sounds. Four different models were trained, a windowed implementation, a windowed and binned implementation, a binned implemenation, and a normal implementation (features were selected over the whole sound sample).


## Data Collection and Preprocessing

Each sample is in its own WAV file which is approximately 30 seconds long. The audio was recorded on an iPad Pro, which saves the audio under a .m4a extension, so each sample was converted to WAV using a converter. The samples are read in and pre-processed for each implementation seperately. For example, the whole windowed implementation will read the WAV files and process them, then the windowed and binned implementation will read and process the files again. 

Median filtering was used to pre-process the signal before features were extracted for all implementations. This was done to reduce the noise from the recording. The median filter size was selected so that important data is not lost due to the filtering.

## Features

```gherkin=
Feature: Guess the word

  # The first example has two steps
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  # The second example has three steps
  Scenario: Breaker joins a game
    Given the Maker has started a game with the word "silky"
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
```
> I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it. [name=Bill Gates]


```gherkin=
Feature: Shopping Cart
  As a Shopper
  I want to put items in my shopping cart
  Because I want to manage items before I check out

  Scenario: User adds item to cart
    Given I'm a logged-in User
    When I go to the Item page
    And I click "Add item to cart"
    Then the quantity of items in my cart should go up
    And my subtotal should increment
    And the warehouse inventory should decrement
```

> Read more about Gherkin here: https://docs.cucumber.io/gherkin/reference/

## Results
```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
Note left of Alice: Alice responds
Alice->Bob: Where have you been?
```

> Read more about sequence-diagrams here: http://bramp.github.io/js-sequence-diagrams/


