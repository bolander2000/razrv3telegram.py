def tod: if type=="number" then strflocaltime("%H:%M") else tostring end;
.message | {"nome":.from.first_name, "date":(.date|tod), "text":.text[0:135], "tipo":.chat.type, "id":.chat.id, "title": .chat.title} 
