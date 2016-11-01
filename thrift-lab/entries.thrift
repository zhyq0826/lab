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

typedef list<User> UserList
typedef list<Entries> EntriesList

struct EntriesResult {
    1: EntriesList entries;
}


const i32 MAX_RESULTS = 100;


service EntriesService {
    EntriesList query_entries(1:i32 page) throws (1:ErrorException error)
}