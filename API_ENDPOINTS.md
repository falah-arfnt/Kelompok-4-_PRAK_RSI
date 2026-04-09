# API Endpoints Documentation

## Overview
Ini adalah dokumentasi lengkap untuk semua API endpoints yang telah diimplementasikan untuk project CRUD RSI. Setiap model memiliki endpoint lengkap untuk operasi CRUD (Create, Read, Update, Delete).

---

## 1. USER Endpoints

### Base URL: `/api/users`

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Mendapatkan semua users |
| GET | `/{user_id}` | Mendapatkan user berdasarkan ID |
| POST | `/` | Membuat user baru |
| PUT | `/{user_id}` | Update seluruh data user |
| PATCH | `/{user_id}` | Update sebagian data user |
| DELETE | `/{user_id}` | Menghapus user |

**Request Body (POST/PUT/PATCH):**
```json
{
  "first_name": "string",
  "last_name": "string",
  "whatsapp": "string"
}
```

---

## 2. ACCOUNT Endpoints

### Base URL: `/api/accounts`

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Mendapatkan semua accounts |
| GET | `/{account_id}` | Mendapatkan account berdasarkan ID |
| POST | `/` | Membuat account baru |
| PUT | `/{account_id}` | Update seluruh data account |
| PATCH | `/{account_id}` | Update sebagian data account |
| DELETE | `/{account_id}` | Menghapus account |

**Request Body (POST/PUT/PATCH):**
```json
{
  "user_id": "integer",
  "role_id": "integer",
  "username": "string",
  "password": "string"
}
```

---

## 3. ROLE Endpoints

### Base URL: `/api/roles`

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Mendapatkan semua roles |
| GET | `/{role_id}` | Mendapatkan role berdasarkan ID |
| POST | `/` | Membuat role baru |
| PUT | `/{role_id}` | Update seluruh data role |
| PATCH | `/{role_id}` | Update sebagian data role |
| DELETE | `/{role_id}` | Menghapus role |

**Request Body (POST/PUT/PATCH):**
```json
{
  "name": "string"
}
```

---

## 4. REGISTRATION Endpoints

### Base URL: `/api/registrations`

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Mendapatkan semua registrations |
| GET | `/{registration_id}` | Mendapatkan registration berdasarkan ID |
| POST | `/` | Membuat registration baru |
| PUT | `/{registration_id}` | Update seluruh data registration |
| PATCH | `/{registration_id}` | Update sebagian data registration |
| DELETE | `/{registration_id}` | Menghapus registration |

**Request Body (POST/PUT/PATCH):**
```json
{
  "user_id": "integer",
  "event_id": "integer"
}
```

---

## 5. EVENT Endpoints

### Base URL: `/api/events`

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Mendapatkan semua events |
| GET | `/{event_id}` | Mendapatkan event berdasarkan ID |
| POST | `/` | Membuat event baru |
| PUT | `/{event_id}` | Update seluruh data event |
| PATCH | `/{event_id}` | Update sebagian data event |
| DELETE | `/{event_id}` | Menghapus event |

**Request Body (POST/PUT/PATCH):**
```json
{
  "name": "string",
  "description": "string",
  "quota": "integer"
}
```

---

## Response Examples

### Success Response (200 OK)
```json
{
  "id": 1,
  "name": "Admin",
  "created_at": "2026-04-09T10:00:00"
}
```

### Error Response (404 Not Found)
```json
{
  "detail": "Role not found"
}
```

---

## HTTP Status Codes

| Code | Deskripsi |
|------|-----------|
| 200 | Success - Request berhasil |
| 201 | Created - Resource berhasil dibuat |
| 400 | Bad Request - Request tidak valid |
| 404 | Not Found - Resource tidak ditemukan |
| 500 | Internal Server Error - Error di server |

---

## Implementation Details

### Architecture Pattern: Layered Architecture
```
Routes (user_router.py, etc.)
    ↓
Controllers (user_controller.py, etc.)
    ↓
Services (user_service.py, etc.)
    ↓
Repositories (user_repository.py, etc.)
    ↓
Database (Schema & Connection)
```

### Files Modified/Created:

#### DTOs (Data Transfer Objects)
- ✅ `src/dto/user_dto.py` - Added UserUpdate
- ✅ `src/dto/account_dto.py` - Added AccountUpdate
- ✅ `src/dto/role_dto.py` - Created with RoleCreate, RoleUpdate, RoleResponse
- ✅ `src/dto/event_dto.py` - Added EventUpdate (added quota field)
- ✅ `src/dto/registration_dto.py` - Created with RegistrationCreate, RegistrationUpdate, RegistrationResponse

#### Repositories
- ✅ `src/repositories/user_repository.py` - Added get_user_by_id, update_user, delete_user
- ✅ `src/repositories/account_repository.py` - Added get_account_by_id, update_account, delete_account
- ✅ `src/repositories/role_repository.py` - Added get_role_by_id, update_role, delete_role
- ✅ `src/repositories/event_repository.py` - Added get_event_by_id, update_event, delete_event
- ✅ `src/repositories/registration_repository.py` - Added get_registration_by_id, update_registration, delete_registration

#### Services
- ✅ `src/services/user_service.py` - Added get_user_by_id, update_user, delete_user
- ✅ `src/services/account_service.py` - Added get_account_by_id, update_account, delete_account
- ✅ `src/services/role_service.py` - Added get_role_by_id, update_role, delete_role
- ✅ `src/services/event_service.py` - Added get_event_by_id, update_event, delete_event
- ✅ `src/services/registration_service.py` - Added get_registration_by_id, update_registration, delete_registration

#### Controllers
- ✅ `src/controllers/user_controller.py` - Added get_user_by_id, update_user, delete_user
- ✅ `src/controllers/account_controller.py` - Added get_account_by_id, update_account, delete_account
- ✅ `src/controllers/role_controller.py` - Converted from router to pure controller functions
- ✅ `src/controllers/event_controller.py` - Added get_event_by_id, update_event, delete_event
- ✅ `src/controllers/registration_controller.py` - Added get_registration_by_id, update_registration, delete_registration

#### Routes
- ✅ `src/routes/user_router.py` - Complete CRUD endpoints with error handling
- ✅ `src/routes/account_router.py` - Complete CRUD endpoints with error handling
- ✅ `src/routes/role_router.py` - Complete CRUD endpoints with error handling
- ✅ `src/routes/registration_router.py` - Complete CRUD endpoints with error handling
- ✅ `src/routes/event_router.py` - Complete CRUD endpoints with error handling

#### Main Application
- ✅ `src/app.py` - Integrated all routers with /api prefix

---

## Testing dengan Curl/Postman

### User Examples:

**GET semua users:**
```bash
curl -X GET http://localhost:8000/api/users
```

**POST user baru:**
```bash
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "whatsapp": "08123456789"
  }'
```

**PUT update user:**
```bash
curl -X PUT http://localhost:8000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jane",
    "last_name": "Smith",
    "whatsapp": "08987654321"
  }'
```

**PATCH partial update user:**
```bash
curl -X PATCH http://localhost:8000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "whatsapp": "08111111111"
  }'
```

**DELETE user:**
```bash
curl -X DELETE http://localhost:8000/api/users/1
```

---

## Catatan Penting

1. **PUT vs PATCH**: 
   - PUT memerlukan semua field
   - PATCH hanya memerlukan field yang ingin diubah

2. **Error Handling**: Semua endpoint telah dilengkapi dengan error handling untuk 404 Not Found

3. **Database Connection**: Pastikan database sudah terkoneksi melalui alembic sebelum menjalankan API

4. **Response Models**: Semua response menggunakan Pydantic models untuk validasi dan dokumentasi

---

## Struktur File Final

```
src/
├── app.py (updated)
├── routes/
│   ├── user_router.py (updated)
│   ├── account_router.py (updated)
│   ├── role_router.py (updated)
│   ├── event_router.py (updated)
│   └── registration_router.py (updated)
├── controllers/
│   ├── user_controller.py (updated)
│   ├── account_controller.py (updated)
│   ├── role_controller.py (updated)
│   ├── event_controller.py (updated)
│   └── registration_controller.py (updated)
├── services/
│   ├── user_service.py (updated)
│   ├── account_service.py (updated)
│   ├── role_service.py (updated)
│   ├── event_service.py (updated)
│   └── registration_service.py (updated)
├── repositories/
│   ├── user_repository.py (updated)
│   ├── account_repository.py (updated)
│   ├── role_repository.py (updated)
│   ├── event_repository.py (updated)
│   └── registration_repository.py (updated)
└── dto/
    ├── user_dto.py (updated)
    ├── account_dto.py (updated)
    ├── role_dto.py (created)
    ├── event_dto.py (updated)
    └── registration_dto.py (created)
```

---

**Status**: ✅ POIN 4 COMPLETED

Semua endpoints CRUD untuk User, Account, Role, Registration, dan Event sudah selesai diimplementasikan dengan standar REST API best practices.
