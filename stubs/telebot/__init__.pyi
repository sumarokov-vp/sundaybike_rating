from _typeshed import Incomplete
from datetime import datetime
from telebot import apihelper as apihelper, types as types, util as util
from telebot.custom_filters import AdvancedCustomFilter as AdvancedCustomFilter, SimpleCustomFilter as SimpleCustomFilter
from telebot.handler_backends import BaseMiddleware as BaseMiddleware, CancelUpdate as CancelUpdate, ContinueHandling as ContinueHandling, FileHandlerBackend as FileHandlerBackend, HandlerBackend as HandlerBackend, MemoryHandlerBackend as MemoryHandlerBackend, SkipHandler as SkipHandler, State as State
from telebot.storage import StateMemoryStorage as StateMemoryStorage, StatePickleStorage as StatePickleStorage, StateStorageBase as StateStorageBase
from typing import Any, Callable, List, Optional, Union

logger: Incomplete
formatter: Incomplete
console_output_handler: Incomplete
REPLY_MARKUP_TYPES = Union[types.InlineKeyboardMarkup, types.ReplyKeyboardMarkup, types.ReplyKeyboardRemove, types.ForceReply]

class Handler:
    callback: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, callback, *args, **kwargs) -> None: ...
    def __getitem__(self, item): ...

class ExceptionHandler:
    def handle(self, exception): ...

class TeleBot:
    token: Incomplete
    skip_pending: Incomplete
    last_update_id: Incomplete
    suppress_middleware_excepions: Incomplete
    parse_mode: Incomplete
    disable_web_page_preview: Incomplete
    disable_notification: Incomplete
    protect_content: Incomplete
    allow_sending_without_reply: Incomplete
    exc_info: Incomplete
    current_states: Incomplete
    next_step_backend: Incomplete
    reply_backend: Incomplete
    exception_handler: Incomplete
    update_listener: Incomplete
    message_handlers: Incomplete
    edited_message_handlers: Incomplete
    channel_post_handlers: Incomplete
    edited_channel_post_handlers: Incomplete
    inline_handlers: Incomplete
    chosen_inline_handlers: Incomplete
    callback_query_handlers: Incomplete
    shipping_query_handlers: Incomplete
    pre_checkout_query_handlers: Incomplete
    poll_handlers: Incomplete
    poll_answer_handlers: Incomplete
    my_chat_member_handlers: Incomplete
    chat_member_handlers: Incomplete
    chat_join_request_handlers: Incomplete
    custom_filters: Incomplete
    state_handlers: Incomplete
    use_class_middlewares: Incomplete
    typed_middleware_handlers: Incomplete
    default_middleware_handlers: Incomplete
    middlewares: Incomplete
    threaded: Incomplete
    worker_pool: Incomplete
    def __init__(self, token: str, parse_mode: Optional[str] = ..., threaded: Optional[bool] = ..., skip_pending: Optional[bool] = ..., num_threads: Optional[int] = ..., next_step_backend: Optional[HandlerBackend] = ..., reply_backend: Optional[HandlerBackend] = ..., exception_handler: Optional[ExceptionHandler] = ..., last_update_id: Optional[int] = ..., suppress_middleware_excepions: Optional[bool] = ..., state_storage: Optional[StateStorageBase] = ..., use_class_middlewares: Optional[bool] = ..., disable_web_page_preview: Optional[bool] = ..., disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., allow_sending_without_reply: Optional[bool] = ..., colorful_logs: Optional[bool] = ...) -> None: ...
    @property
    def user(self) -> types.User: ...
    def enable_save_next_step_handlers(self, delay: Optional[int] = ..., filename: Optional[str] = ...): ...
    def enable_saving_states(self, filename: Optional[str] = ...): ...
    def enable_save_reply_handlers(self, delay: int = ..., filename: str = ...) -> None: ...
    def disable_save_next_step_handlers(self) -> None: ...
    def disable_save_reply_handlers(self) -> None: ...
    def load_next_step_handlers(self, filename: str = ..., del_file_after_loading: bool = ...) -> None: ...
    def load_reply_handlers(self, filename: str = ..., del_file_after_loading: bool = ...) -> None: ...
    def set_webhook(self, url: Optional[str] = ..., certificate: Optional[Union[str, Any]] = ..., max_connections: Optional[int] = ..., allowed_updates: Optional[List[str]] = ..., ip_address: Optional[str] = ..., drop_pending_updates: Optional[bool] = ..., timeout: Optional[int] = ..., secret_token: Optional[str] = ...) -> bool: ...
    webhook_listener: Incomplete
    def run_webhooks(self, listen: Optional[str] = ..., port: Optional[int] = ..., url_path: Optional[str] = ..., certificate: Optional[str] = ..., certificate_key: Optional[str] = ..., webhook_url: Optional[str] = ..., max_connections: Optional[int] = ..., allowed_updates: Optional[List] = ..., ip_address: Optional[str] = ..., drop_pending_updates: Optional[bool] = ..., timeout: Optional[int] = ..., secret_token: Optional[str] = ..., secret_token_length: Optional[int] = ...): ...
    def delete_webhook(self, drop_pending_updates: Optional[bool] = ..., timeout: Optional[int] = ...) -> bool: ...
    def get_webhook_info(self, timeout: Optional[int] = ...) -> types.WebhookInfo: ...
    def remove_webhook(self) -> bool: ...
    def get_updates(self, offset: Optional[int] = ..., limit: Optional[int] = ..., timeout: Optional[int] = ..., allowed_updates: Optional[List[str]] = ..., long_polling_timeout: int = ...) -> List[types.Update]: ...
    def process_new_updates(self, updates: List[types.Update]): ...
    def process_new_messages(self, new_messages) -> None: ...
    def process_new_edited_messages(self, edited_message) -> None: ...
    def process_new_channel_posts(self, channel_post) -> None: ...
    def process_new_edited_channel_posts(self, edited_channel_post) -> None: ...
    def process_new_inline_query(self, new_inline_queries) -> None: ...
    def process_new_chosen_inline_query(self, new_chosen_inline_queries) -> None: ...
    def process_new_callback_query(self, new_callback_queries) -> None: ...
    def process_new_shipping_query(self, new_shipping_queries) -> None: ...
    def process_new_pre_checkout_query(self, pre_checkout_queries) -> None: ...
    def process_new_poll(self, polls) -> None: ...
    def process_new_poll_answer(self, poll_answers) -> None: ...
    def process_new_my_chat_member(self, my_chat_members) -> None: ...
    def process_new_chat_member(self, chat_members) -> None: ...
    def process_new_chat_join_request(self, chat_join_request) -> None: ...
    def process_middlewares(self, update) -> None: ...
    def infinity_polling(self, timeout: Optional[int] = ..., skip_pending: Optional[bool] = ..., long_polling_timeout: Optional[int] = ..., logger_level: Optional[int] = ..., allowed_updates: Optional[List[str]] = ..., restart_on_change: Optional[bool] = ..., path_to_watch: Optional[str] = ..., *args, **kwargs): ...
    def polling(self, non_stop: Optional[bool] = ..., skip_pending: Optional[bool] = ..., interval: Optional[int] = ..., timeout: Optional[int] = ..., long_polling_timeout: Optional[int] = ..., logger_level: Optional[int] = ..., allowed_updates: Optional[List[str]] = ..., none_stop: Optional[bool] = ..., restart_on_change: Optional[bool] = ..., path_to_watch: Optional[str] = ...): ...
    def stop_polling(self) -> None: ...
    def stop_bot(self) -> None: ...
    def set_update_listener(self, listener: Callable): ...
    def get_me(self) -> types.User: ...
    def get_file(self, file_id: Optional[str]) -> types.File: ...
    def get_file_url(self, file_id: Optional[str]) -> str: ...
    def download_file(self, file_path: str) -> bytes: ...
    def log_out(self) -> bool: ...
    def close(self) -> bool: ...
    def get_user_profile_photos(self, user_id: int, offset: Optional[int] = ..., limit: Optional[int] = ...) -> types.UserProfilePhotos: ...
    def get_chat(self, chat_id: Union[int, str]) -> types.Chat: ...
    def leave_chat(self, chat_id: Union[int, str]) -> bool: ...
    def get_chat_administrators(self, chat_id: Union[int, str]) -> List[types.ChatMember]: ...
    def get_chat_members_count(self, chat_id: Union[int, str]) -> int: ...
    def get_chat_member_count(self, chat_id: Union[int, str]) -> int: ...
    def set_chat_sticker_set(self, chat_id: Union[int, str], sticker_set_name: str) -> types.StickerSet: ...
    def delete_chat_sticker_set(self, chat_id: Union[int, str]) -> bool: ...
    def get_chat_member(self, chat_id: Union[int, str], user_id: int) -> types.ChatMember: ...
    def send_message(self, chat_id: Union[int, str], text: str, parse_mode: Optional[str] = ..., entities: Optional[List[types.MessageEntity]] = ..., disable_web_page_preview: Optional[bool] = ..., disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def forward_message(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., timeout: Optional[int] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def copy_message(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, caption: Optional[str] = ..., parse_mode: Optional[str] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., message_thread_id: Optional[int] = ...) -> types.MessageID: ...
    def delete_message(self, chat_id: Union[int, str], message_id: int, timeout: Optional[int] = ...) -> bool: ...
    def send_dice(self, chat_id: Union[int, str], emoji: Optional[str] = ..., disable_notification: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def send_photo(self, chat_id: Union[int, str], photo: Union[Any, str], caption: Optional[str] = ..., parse_mode: Optional[str] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., message_thread_id: Optional[int] = ..., has_spoiler: Optional[bool] = ...) -> types.Message: ...
    def send_audio(self, chat_id: Union[int, str], audio: Union[Any, str], caption: Optional[str] = ..., duration: Optional[int] = ..., performer: Optional[str] = ..., title: Optional[str] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., parse_mode: Optional[str] = ..., disable_notification: Optional[bool] = ..., timeout: Optional[int] = ..., thumbnail: Optional[Union[Any, str]] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ..., thumb: Optional[Union[Any, str]] = ...) -> types.Message: ...
    def send_voice(self, chat_id: Union[int, str], voice: Union[Any, str], caption: Optional[str] = ..., duration: Optional[int] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., parse_mode: Optional[str] = ..., disable_notification: Optional[bool] = ..., timeout: Optional[int] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def send_document(self, chat_id: Union[int, str], document: Union[Any, str], reply_to_message_id: Optional[int] = ..., caption: Optional[str] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., parse_mode: Optional[str] = ..., disable_notification: Optional[bool] = ..., timeout: Optional[int] = ..., thumbnail: Optional[Union[Any, str]] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., allow_sending_without_reply: Optional[bool] = ..., visible_file_name: Optional[str] = ..., disable_content_type_detection: Optional[bool] = ..., data: Optional[Union[Any, str]] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ..., thumb: Optional[Union[Any, str]] = ...) -> types.Message: ...
    def send_sticker(self, chat_id: Union[int, str], sticker: Union[Any, str], reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., disable_notification: Optional[bool] = ..., timeout: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., data: Union[Any, str] = ..., message_thread_id: Optional[int] = ..., emoji: Optional[str] = ...) -> types.Message: ...
    def send_video(self, chat_id: Union[int, str], video: Union[Any, str], duration: Optional[int] = ..., width: Optional[int] = ..., height: Optional[int] = ..., thumbnail: Optional[Union[Any, str]] = ..., caption: Optional[str] = ..., parse_mode: Optional[str] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., supports_streaming: Optional[bool] = ..., disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., data: Optional[Union[Any, str]] = ..., message_thread_id: Optional[int] = ..., has_spoiler: Optional[bool] = ..., thumb: Optional[Union[Any, str]] = ...) -> types.Message: ...
    def send_animation(self, chat_id: Union[int, str], animation: Union[Any, str], duration: Optional[int] = ..., width: Optional[int] = ..., height: Optional[int] = ..., thumbnail: Optional[Union[Any, str]] = ..., caption: Optional[str] = ..., parse_mode: Optional[str] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., message_thread_id: Optional[int] = ..., has_spoiler: Optional[bool] = ..., thumb: Optional[Union[Any, str]] = ...) -> types.Message: ...
    def send_video_note(self, chat_id: Union[int, str], data: Union[Any, str], duration: Optional[int] = ..., length: Optional[int] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., disable_notification: Optional[bool] = ..., timeout: Optional[int] = ..., thumbnail: Optional[Union[Any, str]] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ..., thumb: Optional[Union[Any, str]] = ...) -> types.Message: ...
    def send_media_group(self, chat_id: Union[int, str], media: List[Union[types.InputMediaAudio, types.InputMediaDocument, types.InputMediaPhoto, types.InputMediaVideo]], disable_notification: Optional[bool] = ..., protect_content: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., timeout: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> List[types.Message]: ...
    def send_location(self, chat_id: Union[int, str], latitude: float, longitude: float, live_period: Optional[int] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., disable_notification: Optional[bool] = ..., timeout: Optional[int] = ..., horizontal_accuracy: Optional[float] = ..., heading: Optional[int] = ..., proximity_alert_radius: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def edit_message_live_location(self, latitude: float, longitude: float, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ..., reply_markup: Optional[types.InlineKeyboardMarkup] = ..., timeout: Optional[int] = ..., horizontal_accuracy: Optional[float] = ..., heading: Optional[int] = ..., proximity_alert_radius: Optional[int] = ...) -> None: ...
    def stop_message_live_location(self, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ..., reply_markup: Optional[types.InlineKeyboardMarkup] = ..., timeout: Optional[int] = ...) -> None: ...
    def send_venue(self, chat_id: Union[int, str], latitude: Optional[float], longitude: Optional[float], title: str, address: str, foursquare_id: Optional[str] = ..., foursquare_type: Optional[str] = ..., disable_notification: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., google_place_id: Optional[str] = ..., google_place_type: Optional[str] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def send_contact(self, chat_id: Union[int, str], phone_number: str, first_name: str, last_name: Optional[str] = ..., vcard: Optional[str] = ..., disable_notification: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def send_chat_action(self, chat_id: Union[int, str], action: str, timeout: Optional[int] = ..., message_thread_id: Optional[int] = ...) -> bool: ...
    def kick_chat_member(self, chat_id: Union[int, str], user_id: int, until_date: Optional[Union[int, datetime]] = ..., revoke_messages: Optional[bool] = ...) -> bool: ...
    def ban_chat_member(self, chat_id: Union[int, str], user_id: int, until_date: Optional[Union[int, datetime]] = ..., revoke_messages: Optional[bool] = ...) -> bool: ...
    def unban_chat_member(self, chat_id: Union[int, str], user_id: int, only_if_banned: Optional[bool] = ...) -> bool: ...
    def restrict_chat_member(self, chat_id: Union[int, str], user_id: int, until_date: Optional[Union[int, datetime]] = ..., can_send_messages: Optional[bool] = ..., can_send_media_messages: Optional[bool] = ..., can_send_polls: Optional[bool] = ..., can_send_other_messages: Optional[bool] = ..., can_add_web_page_previews: Optional[bool] = ..., can_change_info: Optional[bool] = ..., can_invite_users: Optional[bool] = ..., can_pin_messages: Optional[bool] = ..., permissions: Optional[types.ChatPermissions] = ..., use_independent_chat_permissions: Optional[bool] = ...) -> bool: ...
    def promote_chat_member(self, chat_id: Union[int, str], user_id: int, can_change_info: Optional[bool] = ..., can_post_messages: Optional[bool] = ..., can_edit_messages: Optional[bool] = ..., can_delete_messages: Optional[bool] = ..., can_invite_users: Optional[bool] = ..., can_restrict_members: Optional[bool] = ..., can_pin_messages: Optional[bool] = ..., can_promote_members: Optional[bool] = ..., is_anonymous: Optional[bool] = ..., can_manage_chat: Optional[bool] = ..., can_manage_video_chats: Optional[bool] = ..., can_manage_voice_chats: Optional[bool] = ..., can_manage_topics: Optional[bool] = ..., can_post_stories: Optional[bool] = ..., can_edit_stories: Optional[bool] = ..., can_delete_stories: Optional[bool] = ...) -> bool: ...
    def set_chat_administrator_custom_title(self, chat_id: Union[int, str], user_id: int, custom_title: str) -> bool: ...
    def ban_chat_sender_chat(self, chat_id: Union[int, str], sender_chat_id: Union[int, str]) -> bool: ...
    def unban_chat_sender_chat(self, chat_id: Union[int, str], sender_chat_id: Union[int, str]) -> bool: ...
    def set_chat_permissions(self, chat_id: Union[int, str], permissions: types.ChatPermissions, use_independent_chat_permissions: Optional[bool] = ...) -> bool: ...
    def create_chat_invite_link(self, chat_id: Union[int, str], name: Optional[str] = ..., expire_date: Optional[Union[int, datetime]] = ..., member_limit: Optional[int] = ..., creates_join_request: Optional[bool] = ...) -> types.ChatInviteLink: ...
    def edit_chat_invite_link(self, chat_id: Union[int, str], invite_link: Optional[str] = ..., name: Optional[str] = ..., expire_date: Optional[Union[int, datetime]] = ..., member_limit: Optional[int] = ..., creates_join_request: Optional[bool] = ...) -> types.ChatInviteLink: ...
    def revoke_chat_invite_link(self, chat_id: Union[int, str], invite_link: str) -> types.ChatInviteLink: ...
    def export_chat_invite_link(self, chat_id: Union[int, str]) -> str: ...
    def approve_chat_join_request(self, chat_id: Union[str, int], user_id: Union[int, str]) -> bool: ...
    def decline_chat_join_request(self, chat_id: Union[str, int], user_id: Union[int, str]) -> bool: ...
    def set_chat_photo(self, chat_id: Union[int, str], photo: Any) -> bool: ...
    def delete_chat_photo(self, chat_id: Union[int, str]) -> bool: ...
    def get_my_commands(self, scope: Optional[types.BotCommandScope] = ..., language_code: Optional[str] = ...) -> List[types.BotCommand]: ...
    def set_my_name(self, name: Optional[str] = ..., language_code: Optional[str] = ...): ...
    def get_my_name(self, language_code: Optional[str] = ...): ...
    def set_my_description(self, description: Optional[str] = ..., language_code: Optional[str] = ...): ...
    def get_my_description(self, language_code: Optional[str] = ...): ...
    def set_my_short_description(self, short_description: Optional[str] = ..., language_code: Optional[str] = ...): ...
    def get_my_short_description(self, language_code: Optional[str] = ...): ...
    def set_chat_menu_button(self, chat_id: Union[int, str] = ..., menu_button: types.MenuButton = ...) -> bool: ...
    def get_chat_menu_button(self, chat_id: Union[int, str] = ...) -> types.MenuButton: ...
    def set_my_default_administrator_rights(self, rights: types.ChatAdministratorRights = ..., for_channels: Optional[bool] = ...) -> bool: ...
    def get_my_default_administrator_rights(self, for_channels: Optional[bool] = ...) -> types.ChatAdministratorRights: ...
    def set_my_commands(self, commands: List[types.BotCommand], scope: Optional[types.BotCommandScope] = ..., language_code: Optional[str] = ...) -> bool: ...
    def delete_my_commands(self, scope: Optional[types.BotCommandScope] = ..., language_code: Optional[str] = ...) -> bool: ...
    def set_chat_title(self, chat_id: Union[int, str], title: str) -> bool: ...
    def set_chat_description(self, chat_id: Union[int, str], description: Optional[str] = ...) -> bool: ...
    def pin_chat_message(self, chat_id: Union[int, str], message_id: int, disable_notification: Optional[bool] = ...) -> bool: ...
    def unpin_chat_message(self, chat_id: Union[int, str], message_id: Optional[int] = ...) -> bool: ...
    def unpin_all_chat_messages(self, chat_id: Union[int, str]) -> bool: ...
    def edit_message_text(self, text: str, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ..., parse_mode: Optional[str] = ..., entities: Optional[List[types.MessageEntity]] = ..., disable_web_page_preview: Optional[bool] = ..., reply_markup: Optional[types.InlineKeyboardMarkup] = ...) -> Union[types.Message, bool]: ...
    def edit_message_media(self, media: Any, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ..., reply_markup: Optional[types.InlineKeyboardMarkup] = ...) -> Union[types.Message, bool]: ...
    def edit_message_reply_markup(self, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ..., reply_markup: Optional[types.InlineKeyboardMarkup] = ...) -> Union[types.Message, bool]: ...
    def send_game(self, chat_id: Union[int, str], game_short_name: str, disable_notification: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., timeout: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def set_game_score(self, user_id: Union[int, str], score: int, force: Optional[bool] = ..., chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ..., disable_edit_message: Optional[bool] = ...) -> Union[types.Message, bool]: ...
    def get_game_high_scores(self, user_id: int, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ...) -> List[types.GameHighScore]: ...
    def send_invoice(self, chat_id: Union[int, str], title: str, description: str, invoice_payload: str, provider_token: str, currency: str, prices: List[types.LabeledPrice], start_parameter: Optional[str] = ..., photo_url: Optional[str] = ..., photo_size: Optional[int] = ..., photo_width: Optional[int] = ..., photo_height: Optional[int] = ..., need_name: Optional[bool] = ..., need_phone_number: Optional[bool] = ..., need_email: Optional[bool] = ..., need_shipping_address: Optional[bool] = ..., send_phone_number_to_provider: Optional[bool] = ..., send_email_to_provider: Optional[bool] = ..., is_flexible: Optional[bool] = ..., disable_notification: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., provider_data: Optional[str] = ..., timeout: Optional[int] = ..., allow_sending_without_reply: Optional[bool] = ..., max_tip_amount: Optional[int] = ..., suggested_tip_amounts: Optional[List[int]] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def create_invoice_link(self, title: str, description: str, payload: str, provider_token: str, currency: str, prices: List[types.LabeledPrice], max_tip_amount: Optional[int] = ..., suggested_tip_amounts: Optional[List[int]] = ..., provider_data: Optional[str] = ..., photo_url: Optional[str] = ..., photo_size: Optional[int] = ..., photo_width: Optional[int] = ..., photo_height: Optional[int] = ..., need_name: Optional[bool] = ..., need_phone_number: Optional[bool] = ..., need_email: Optional[bool] = ..., need_shipping_address: Optional[bool] = ..., send_phone_number_to_provider: Optional[bool] = ..., send_email_to_provider: Optional[bool] = ..., is_flexible: Optional[bool] = ...) -> str: ...
    def send_poll(self, chat_id: Union[int, str], question: str, options: List[str], is_anonymous: Optional[bool] = ..., type: Optional[str] = ..., allows_multiple_answers: Optional[bool] = ..., correct_option_id: Optional[int] = ..., explanation: Optional[str] = ..., explanation_parse_mode: Optional[str] = ..., open_period: Optional[int] = ..., close_date: Optional[Union[int, datetime]] = ..., is_closed: Optional[bool] = ..., disable_notification: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[REPLY_MARKUP_TYPES] = ..., allow_sending_without_reply: Optional[bool] = ..., timeout: Optional[int] = ..., explanation_entities: Optional[List[types.MessageEntity]] = ..., protect_content: Optional[bool] = ..., message_thread_id: Optional[int] = ...) -> types.Message: ...
    def stop_poll(self, chat_id: Union[int, str], message_id: int, reply_markup: Optional[types.InlineKeyboardMarkup] = ...) -> types.Poll: ...
    def answer_shipping_query(self, shipping_query_id: str, ok: bool, shipping_options: Optional[List[types.ShippingOption]] = ..., error_message: Optional[str] = ...) -> bool: ...
    def answer_pre_checkout_query(self, pre_checkout_query_id: int, ok: bool, error_message: Optional[str] = ...) -> bool: ...
    def edit_message_caption(self, caption: str, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[str] = ..., parse_mode: Optional[str] = ..., caption_entities: Optional[List[types.MessageEntity]] = ..., reply_markup: Optional[types.InlineKeyboardMarkup] = ...) -> Union[types.Message, bool]: ...
    def reply_to(self, message: types.Message, text: str, **kwargs) -> types.Message: ...
    def answer_inline_query(self, inline_query_id: str, results: List[Any], cache_time: Optional[int] = ..., is_personal: Optional[bool] = ..., next_offset: Optional[str] = ..., switch_pm_text: Optional[str] = ..., switch_pm_parameter: Optional[str] = ..., button: Optional[types.InlineQueryResultsButton] = ...) -> bool: ...
    def unpin_all_general_forum_topic_messages(self, chat_id: Union[int, str]) -> bool: ...
    def answer_callback_query(self, callback_query_id: int, text: Optional[str] = ..., show_alert: Optional[bool] = ..., url: Optional[str] = ..., cache_time: Optional[int] = ...) -> bool: ...
    def set_sticker_set_thumbnail(self, name: str, user_id: int, thumbnail: Union[Any, str] = ...): ...
    def set_sticker_set_thumb(self, name: str, user_id: int, thumb: Union[Any, str] = ...): ...
    def get_sticker_set(self, name: str) -> types.StickerSet: ...
    def get_custom_emoji_stickers(self, custom_emoji_ids: List[str]) -> List[types.Sticker]: ...
    def set_sticker_keywords(self, sticker: str, keywords: List[str] = ...) -> bool: ...
    def set_sticker_mask_position(self, sticker: str, mask_position: types.MaskPosition = ...) -> bool: ...
    def set_custom_emoji_sticker_set_thumbnail(self, name: str, custom_emoji_id: Optional[str] = ...) -> bool: ...
    def set_sticker_set_title(self, name: str, title: str) -> bool: ...
    def delete_sticker_set(self, name: str) -> bool: ...
    def set_sticker_emoji_list(self, sticker: str, emoji_list: List[str]) -> bool: ...
    def upload_sticker_file(self, user_id: int, png_sticker: Union[Any, str] = ..., sticker: Optional[types.InputFile] = ..., sticker_format: Optional[str] = ...) -> types.File: ...
    def create_new_sticker_set(self, user_id: int, name: str, title: str, emojis: Optional[List[str]] = ..., png_sticker: Union[Any, str] = ..., tgs_sticker: Union[Any, str] = ..., webm_sticker: Union[Any, str] = ..., contains_masks: Optional[bool] = ..., sticker_type: Optional[str] = ..., mask_position: Optional[types.MaskPosition] = ..., needs_repainting: Optional[bool] = ..., stickers: List[types.InputSticker] = ..., sticker_format: Optional[str] = ...) -> bool: ...
    def add_sticker_to_set(self, user_id: int, name: str, emojis: Union[List[str], str], png_sticker: Optional[Union[Any, str]] = ..., tgs_sticker: Optional[Union[Any, str]] = ..., webm_sticker: Optional[Union[Any, str]] = ..., mask_position: Optional[types.MaskPosition] = ..., sticker: Optional[List[types.InputSticker]] = ...) -> bool: ...
    def set_sticker_position_in_set(self, sticker: str, position: int) -> bool: ...
    def delete_sticker_from_set(self, sticker: str) -> bool: ...
    def create_forum_topic(self, chat_id: int, name: str, icon_color: Optional[int] = ..., icon_custom_emoji_id: Optional[str] = ...) -> types.ForumTopic: ...
    def edit_forum_topic(self, chat_id: Union[int, str], message_thread_id: int, name: Optional[str] = ..., icon_custom_emoji_id: Optional[str] = ...) -> bool: ...
    def close_forum_topic(self, chat_id: Union[str, int], message_thread_id: int) -> bool: ...
    def reopen_forum_topic(self, chat_id: Union[str, int], message_thread_id: int) -> bool: ...
    def delete_forum_topic(self, chat_id: Union[str, int], message_thread_id: int) -> bool: ...
    def unpin_all_forum_topic_messages(self, chat_id: Union[str, int], message_thread_id: int) -> bool: ...
    def edit_general_forum_topic(self, chat_id: Union[int, str], name: str) -> bool: ...
    def close_general_forum_topic(self, chat_id: Union[int, str]) -> bool: ...
    def reopen_general_forum_topic(self, chat_id: Union[int, str]) -> bool: ...
    def hide_general_forum_topic(self, chat_id: Union[int, str]) -> bool: ...
    def unhide_general_forum_topic(self, chat_id: Union[int, str]) -> bool: ...
    def get_forum_topic_icon_stickers(self) -> List[types.Sticker]: ...
    def answer_web_app_query(self, web_app_query_id: str, result: types.InlineQueryResultBase) -> types.SentWebAppMessage: ...
    def register_for_reply(self, message: types.Message, callback: Callable, *args, **kwargs) -> None: ...
    def register_for_reply_by_message_id(self, message_id: int, callback: Callable, *args, **kwargs) -> None: ...
    def register_next_step_handler(self, message: types.Message, callback: Callable, *args, **kwargs) -> None: ...
    def setup_middleware(self, middleware: BaseMiddleware): ...
    def set_state(self, user_id: int, state: Union[int, str, State], chat_id: Optional[int] = ...) -> None: ...
    def reset_data(self, user_id: int, chat_id: Optional[int] = ...): ...
    def delete_state(self, user_id: int, chat_id: Optional[int] = ...) -> None: ...
    def retrieve_data(self, user_id: int, chat_id: Optional[int] = ...) -> Optional[Any]: ...
    def get_state(self, user_id: int, chat_id: Optional[int] = ...) -> Optional[Union[int, str, State]]: ...
    def add_data(self, user_id: int, chat_id: Optional[int] = ..., **kwargs): ...
    def register_next_step_handler_by_chat_id(self, chat_id: int, callback: Callable, *args, **kwargs) -> None: ...
    def clear_step_handler(self, message: types.Message) -> None: ...
    def clear_step_handler_by_chat_id(self, chat_id: Union[int, str]) -> None: ...
    def clear_reply_handlers(self, message: types.Message) -> None: ...
    def clear_reply_handlers_by_message_id(self, message_id: int) -> None: ...
    def middleware_handler(self, update_types: Optional[List[str]] = ...): ...
    def add_middleware_handler(self, handler, update_types: Incomplete | None = ...) -> None: ...
    def register_middleware_handler(self, callback, update_types: Incomplete | None = ...) -> None: ...
    @staticmethod
    def check_commands_input(commands, method_name) -> None: ...
    @staticmethod
    def check_regexp_input(regexp, method_name) -> None: ...
    def message_handler(self, commands: Optional[List[str]] = ..., regexp: Optional[str] = ..., func: Optional[Callable] = ..., content_types: Optional[List[str]] = ..., chat_types: Optional[List[str]] = ..., **kwargs): ...
    def add_message_handler(self, handler_dict) -> None: ...
    def register_message_handler(self, callback: Callable, content_types: Optional[List[str]] = ..., commands: Optional[List[str]] = ..., regexp: Optional[str] = ..., func: Optional[Callable] = ..., chat_types: Optional[List[str]] = ..., pass_bot: Optional[bool] = ..., **kwargs): ...
    def edited_message_handler(self, commands: Incomplete | None = ..., regexp: Incomplete | None = ..., func: Incomplete | None = ..., content_types: Incomplete | None = ..., chat_types: Incomplete | None = ..., **kwargs): ...
    def add_edited_message_handler(self, handler_dict) -> None: ...
    def register_edited_message_handler(self, callback: Callable, content_types: Optional[List[str]] = ..., commands: Optional[List[str]] = ..., regexp: Optional[str] = ..., func: Optional[Callable] = ..., chat_types: Optional[List[str]] = ..., pass_bot: Optional[bool] = ..., **kwargs): ...
    def channel_post_handler(self, commands: Incomplete | None = ..., regexp: Incomplete | None = ..., func: Incomplete | None = ..., content_types: Incomplete | None = ..., **kwargs): ...
    def add_channel_post_handler(self, handler_dict) -> None: ...
    def register_channel_post_handler(self, callback: Callable, content_types: Optional[List[str]] = ..., commands: Optional[List[str]] = ..., regexp: Optional[str] = ..., func: Optional[Callable] = ..., pass_bot: Optional[bool] = ..., **kwargs): ...
    def edited_channel_post_handler(self, commands: Incomplete | None = ..., regexp: Incomplete | None = ..., func: Incomplete | None = ..., content_types: Incomplete | None = ..., **kwargs): ...
    def add_edited_channel_post_handler(self, handler_dict) -> None: ...
    def register_edited_channel_post_handler(self, callback: Callable, content_types: Optional[List[str]] = ..., commands: Optional[List[str]] = ..., regexp: Optional[str] = ..., func: Optional[Callable] = ..., pass_bot: Optional[bool] = ..., **kwargs): ...
    def inline_handler(self, func, **kwargs): ...
    def add_inline_handler(self, handler_dict) -> None: ...
    def register_inline_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = ..., **kwargs): ...
    def chosen_inline_handler(self, func, **kwargs): ...
    def add_chosen_inline_handler(self, handler_dict) -> None: ...
    def register_chosen_inline_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = ..., **kwargs): ...
    def callback_query_handler(self, func, **kwargs): ...
    def add_callback_query_handler(self, handler_dict) -> None: ...
    def register_callback_query_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = ..., **kwargs): ...
    def shipping_query_handler(self, func, **kwargs): ...
    def add_shipping_query_handler(self, handler_dict) -> None: ...
    def register_shipping_query_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = ..., **kwargs): ...
    def pre_checkout_query_handler(self, func, **kwargs): ...
    def add_pre_checkout_query_handler(self, handler_dict) -> None: ...
    def register_pre_checkout_query_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = ..., **kwargs): ...
    def poll_handler(self, func, **kwargs): ...
    def add_poll_handler(self, handler_dict) -> None: ...
    def register_poll_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = ..., **kwargs): ...
    def poll_answer_handler(self, func: Incomplete | None = ..., **kwargs): ...
    def add_poll_answer_handler(self, handler_dict) -> None: ...
    def register_poll_answer_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = ..., **kwargs): ...
    def my_chat_member_handler(self, func: Incomplete | None = ..., **kwargs): ...
    def add_my_chat_member_handler(self, handler_dict) -> None: ...
    def register_my_chat_member_handler(self, callback: Callable, func: Optional[Callable] = ..., pass_bot: Optional[bool] = ..., **kwargs): ...
    def chat_member_handler(self, func: Incomplete | None = ..., **kwargs): ...
    def add_chat_member_handler(self, handler_dict) -> None: ...
    def register_chat_member_handler(self, callback: Callable, func: Optional[Callable] = ..., pass_bot: Optional[bool] = ..., **kwargs): ...
    def chat_join_request_handler(self, func: Incomplete | None = ..., **kwargs): ...
    def add_chat_join_request_handler(self, handler_dict) -> None: ...
    def register_chat_join_request_handler(self, callback: Callable, func: Optional[Callable] = ..., pass_bot: Optional[bool] = ..., **kwargs): ...
    def add_custom_filter(self, custom_filter: Union[SimpleCustomFilter, AdvancedCustomFilter]): ...
