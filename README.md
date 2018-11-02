Todo APP の仕様
=====================

## APP 紹介 ##
シンプルなTodo APPである
SlackからのユーザのInputを受け、
それにResponseするBackend APP
言語はPython、FlameworkはFlaskとする （多分）

Slack bot will interact with your chat to help your todo management

AVAILABLE COMMANDS:
>add(3), update(4), delete(5), show(1), done(4), undone(4), n/a(4)

RESPONSE EXAMPLE:
```
 Id  Due Date     Team Status    daul       Task
----  -----------  ----------  ----------   --------------------------------
  1    Nov,02,2018  9/13         complete   Health_Consciousness_Survey
  2    Nov,01,2018  0/13         pending    GERP_Work_Time_July_2018_Part
```
  
## API List ##


`1. GET /tasks`   
`2. GET /task/<id>`     
`3. POST /tasks`   
`4. POST /tasks/<id>`  
`5. DELETE /task/<id>`  

Delete does not "Delete" actual db record?
db record to is_deleted

### 1. List all Todo tasks ###

**Definition**

`GET /tasks`

**Response**

- `200 OK` when success

```json
[
	{
        "id":"1",
        "item":"Training Preps #1",
        "user1":"complete",
        "user2":"pending",
        "user3":"N/A",
        ...
	},
	{
	    "id":"2",
	    "item":"Training Preps #2"
        "user1":"pending",
        "user2":"complete",
        "user3":"N/A",
        ...
    }
]
```

### 2. Get a Todo Item ###

**Definition**

`GET /tasks/<id>`

**Response**

- `200 OK` when success
- `404 Not Found` if id is not existing

```json
{
    "id":"id1234",
    "item":"Training Preps #1",
    "due":"2018-09-01",
    "user1":"complete",
    "user2":"pending",
    "user3":"N/A"
}
```

- Slack Bot will count team's status as well

### 3. Insert a Todo Item ###

**Definition**

`POST /tasks`

**Arguments**

- `"item":string` context of todo item
- `"due":string` due date of todo item

**Response**

- `201 Created` when success

```json
{
    "id":"1",
    "item":"Training Preps #1",
    "due":"2018-09-20"
}
```

- `400 non acceptable` when arguments are incorrect

- BOT sends message that "Error: Sample: $task-name(spaces not allowed) $due-date"

- `401 permission error` when user is not an admin

- BOT sends message that "Error: You do not have right permission to run this"

### 4. Update a Todo Item ###

**Definition**

`POST /tasks/<id>`

**Arguments**

- `"item":string` context of todo item
- `"due":string` due date of todo item

**Response**

- `200 Success` when success

```json
{
    "id":"1",
    "item":"Training Preps #1",
    "due":"2018-09-20"
}
```

- `400 non acceptable` when arguments are incorrect

- BOT sends message that "Error: Sample: $task-id $task-name(spaces not allowed) $due-date"

- `401 permission error` when user is not an admin

- BOT sends message that "Error: You do not have right permission to run this"

### 5. Delete a Todo Item ###

**Definition**

`DELETE /tasks/<id>`

**Arguments**

- `"id":integer` identifier of todo item

**Response**

- `204 No Content` when success
- BOT sends message that "The task id=xx has been deleted"
- `401 permission error` when user is not an admin
- BOT sends message that "Error: You do not have right permission to run this"
- `404 Not Found` if id is not exsiting
- BOT sends message that "Error: Task ID=xx is not exsiting"