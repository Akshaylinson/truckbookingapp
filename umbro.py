`











﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]














﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]











﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]









﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]










﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]











﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]











﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]










﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]













﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]














﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]











﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]









﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]










﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]











﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]











﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]










﻿from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.models import BookingStatus, PaymentStatus, SeatStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class UserCreate(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=8)
    role: UserRole = UserRole.user


class UserRead(BaseModel):
    id: int
    email: str
    role: UserRole
    created_at: datetime

    model_config = {'from_attributes': True}


class LoginRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str


class EventCreate(BaseModel):
    title: str
    description: str = ''
    venue: str
    starts_at: datetime
    seat_numbers: list[str] | None = None
    seat_count: int = Field(default=0, ge=0)
    price_per_seat: float = Field(default=250.0, ge=0)


class EventRead(BaseModel):
    id: int
    title: str
    description: str
    venue: str
    starts_at: datetime
    total_seats: int
    created_by: int | None

    model_config = {'from_attributes': True}


class SeatRead(BaseModel):
    id: int
    event_id: int
    seat_number: str
    status: SeatStatus
    reserved_by_user_id: int | None
    reserved_until: datetime | None

    model_config = {'from_attributes': True}


class BookingRequestCreate(BaseModel):
    event_id: int
    seat_numbers: list[str]
    idempotency_key: str
    payment_method: str = 'demo'


class BookingRequestRead(BaseModel):
    id: int
    user_id: int
    event_id: int
    idempotency_key: str
    seat_numbers_json: list[str]
    payment_method: str
    status: BookingStatus
    queue_position: int
    booking_id: int | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {'from_attributes': True}


class BookingSeatRead(BaseModel):
    seat_id: int
    seat_number: str
    price: float


class PaymentRead(BaseModel):
    id: int
    booking_id: int
    provider: str
    status: PaymentStatus
    amount: float
    transaction_ref: str | None

    model_config = {'from_attributes': True}


class BookingRead(BaseModel):
    id: int
    booking_ref: str
    user_id: int
    event_id: int
    idempotency_key: str
    status: BookingStatus
    total_amount: float
    created_at: datetime
    confirmed_at: datetime | None
    cancelled_at: datetime | None
    seats: list[BookingSeatRead] = []
    payment: PaymentRead | None = None

    model_config = {'from_attributes': True}


class BookingQueueResponse(BaseModel):
    request_id: int
    status: BookingStatus
    queue_position: int
    message: str


class AdminOverview(BaseModel):
    active_users: int
    queue_length: int
    worker_status: str
    bookings_confirmed: int
    bookings_failed: int
    duplicate_booking_attempts: int
    seat_occupancy: float
    redis_health: str
    database_health: str


class HealthResponse(BaseModel):
    status: str
    service: str


class MetricsResponse(BaseModel):
    metrics: dict[str, int | float]









