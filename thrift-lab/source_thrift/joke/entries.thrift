namespace cpp thrift.example
namespace java thrift.example

enum UserType {
    GIRL,
    BOY
}

struct Location {
    1: required double latitude;
    2: required double longitude;
}

struct User {
    1: required i32 userId;
    2: required string userName;
    3: required string text;
    4: optional Location loc;
    5: optional UserType userType = UserType.BOY;
    16: optional string language = "english";
}

struct Entries {
    1: required string title;
    2: required string text;
    3: required i32 atime;
    4: required User user;
}

exception ErrorException {
    1: i32 code;
    2: string msg;
}

#this has no impact in python
typedef list<User> UserList
typedef list<Entries> EntriesList

struct EntriesResult {
    1: EntriesList entries;
}


const i32 MAX_RESULTS = 100;


#in python the return type must be declared as container explicit
service Joke {
    list<Entries> query_entries(1:i32 page) throws (1:ErrorException error),

    map<i32, User> query_users() throws (1:ErrorException error),

    set<User> query_hot_users(),

    #syntax error
    #list query_cold_users(),

    i32 add(1:i32 num1, 2:i32 num2),

    void ping()
}