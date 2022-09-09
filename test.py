def close():
    return
    def get_chat_menu_button(self, chat_id: Union[int, str]=None) -> types.MenuButton:
        """
        Use this method to get the current value of the bot's menu button
        in a private chat, or the default menu button.
        Returns MenuButton on success.

        Telegram Documentation: https://core.telegram.org/bots/api#getchatmenubutton

        :param chat_id: Unique identifier for the target private chat.
            If not specified, default bot's menu button will be returned.
        :type chat_id: :obj:`int` or :obj:`str`

        :return: types.MenuButton
        :rtype: :class:`telebot.types.MenuButton`
        """
        return types.MenuButton.de_json(apihelper.get_chat_menu_button(self.token, chat_id))





    def set_chat_menu_button(self, chat_id: Union[int, str]=None, 
                menu_button: types.MenuButton=None) -> bool:
        """
        Use this method to change the bot's menu button in a private chat, 
        or the default menu button. 
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatmenubutton

        :param chat_id: Unique identifier for the target private chat. 
            If not specified, default bot's menu button will be changed.
        :type chat_id: :obj:`int` or :obj:`str`

        :param menu_button: A JSON-serialized object for the new bot's menu button. Defaults to MenuButtonDefault
        :type menu_button: :class:`telebot.types.MenuButton`

        :return: True on success.
        :rtype: :obj:`bool`
        """
        return apihelper.set_chat_menu_button(self.token, chat_id, menu_button)
    def set_my_commands(self, commands: List[types.BotCommand],
            scope: Optional[types.BotCommandScope]=None,
            language_code: Optional[str]=None) -> bool:
        """
        Use this method to change the list of the bot's commands.

        Telegram documentation: https://core.telegram.org/bots/api#setmycommands

        :param commands: List of BotCommand. At most 100 commands can be specified.
        :type commands: :obj:`list` of :class:`telebot.types.BotCommand`

        :param scope: The scope of users for which the commands are relevant. 
            Defaults to BotCommandScopeDefault.
        :type scope: :class:`telebot.types.BotCommandScope`

        :param language_code: A two-letter ISO 639-1 language code. If empty, 
            commands will be applied to all users from the given scope, 
            for whose language there are no dedicated commands
        :type language_code: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """
        return apihelper.set_my_commands(self.token, commands, scope, language_code)
    
    def delete_my_commands(self, scope: Optional[types.BotCommandScope]=None, 
            language_code: Optional[str]=None) -> bool:
        """
        Use this method to delete the list of the bot's commands for the given scope and user language. 
        After deletion, higher level commands will be shown to affected users. 
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletemycommands
        
        :param scope: The scope of users for which the commands are relevant. 
            Defaults to BotCommandScopeDefault.
        :type scope: :class:`telebot.types.BotCommandScope`

        :param language_code: A two-letter ISO 639-1 language code. If empty, 
            commands will be applied to all users from the given scope, 
            for whose language there are no dedicated commands
        :type language_code: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """
        return apihelper.delete_my_commands(self.token, scope, language_code)

    def set_chat_title(self, chat_id: Union[int, str], title: str) -> bool:
        """
        Use this method to change the title of a chat. Titles can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.
        Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’
        setting is off in the target group.

        Telegram documentation: https://core.telegram.org/bots/api#setchattitle

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param title: New chat title, 1-255 characters
        :type title: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """
        return apihelper.set_chat_title(self.token, chat_id, title)

    def set_chat_description(self, chat_id: Union[int, str], description: Optional[str]=None) -> bool:
        """
        Use this method to change the description of a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#setchatdescription

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param description: Str: New chat description, 0-255 characters
        :type description: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """
        return apihelper.set_chat_description(self.token, chat_id, description)
    def edit_message_text(
            self, text: str, 
            chat_id: Optional[Union[int, str]]=None, 
            message_id: Optional[int]=None, 
            inline_message_id: Optional[str]=None, 
            parse_mode: Optional[str]=None,
            entities: Optional[List[types.MessageEntity]]=None,
            disable_web_page_preview: Optional[bool]=None,
            reply_markup: Optional[REPLY_MARKUP_TYPES]=None) -> Union[types.Message, bool]:
        """
        Use this method to edit text and game messages.

        Telegram documentation: https://core.telegram.org/bots/api#editmessagetext

        :param text: New text of the message, 1-4096 characters after entities parsing
        :type text: :obj:`str`

        :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Required if inline_message_id is not specified. Identifier of the sent message
        :type message_id: :obj:`int`

        :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type inline_message_id: :obj:`str`

        :param parse_mode: Mode for parsing entities in the message text.
        :type parse_mode: :obj:`str`

        :param entities: List of special entities that appear in the message text, which can be specified instead of parse_mode
        :type entities: List of :obj:`telebot.types.MessageEntity`

        :param disable_web_page_preview: Disables link previews for links in this message
        :type disable_web_page_preview: :obj:`bool`

        :param reply_markup: A JSON-serialized object for an inline keyboard.
        :type reply_markup: :obj:`InlineKeyboardMarkup`

        :return: On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.
        :rtype: :obj:`types.Message` or :obj:`bool`
        """
        parse_mode = self.parse_mode if (parse_mode is None) else parse_mode

        result = apihelper.edit_message_text(self.token, text, chat_id, message_id, inline_message_id, parse_mode,
                                             entities, disable_web_page_preview, reply_markup)
        if type(result) == bool:  # if edit inline message return is bool not Message.
            return result
        return types.Message.de_json(result)

    def send_invoice(
            self, chat_id: Union[int, str], title: str, description: str, 
            invoice_payload: str, provider_token: str, currency: str, 
            prices: List[types.LabeledPrice], start_parameter: Optional[str]=None, 
            photo_url: Optional[str]=None, photo_size: Optional[int]=None, 
            photo_width: Optional[int]=None, photo_height: Optional[int]=None,
            need_name: Optional[bool]=None, need_phone_number: Optional[bool]=None, 
            need_email: Optional[bool]=None, need_shipping_address: Optional[bool]=None,
            send_phone_number_to_provider: Optional[bool]=None, 
            send_email_to_provider: Optional[bool]=None, 
            is_flexible: Optional[bool]=None,
            disable_notification: Optional[bool]=None, 
            reply_to_message_id: Optional[int]=None, 
            reply_markup: Optional[REPLY_MARKUP_TYPES]=None, 
            provider_data: Optional[str]=None, 
            timeout: Optional[int]=None,
            allow_sending_without_reply: Optional[bool]=None,
            max_tip_amount: Optional[int] = None,
            suggested_tip_amounts: Optional[List[int]]=None,
            protect_content: Optional[bool]=None) -> types.Message:
        """
        Sends invoice.

        Telegram documentation: https://core.telegram.org/bots/api#sendinvoice

        :param chat_id: Unique identifier for the target private chat
        :type chat_id: :obj:`int` or :obj:`str`

        :param title: Product name, 1-32 characters
        :type title: :obj:`str`

        :param description: Product description, 1-255 characters
        :type description: :obj:`str`

        :param invoice_payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
            use for your internal processes.
        :type invoice_payload: :obj:`str`

        :param provider_token: Payments provider token, obtained via @Botfather
        :type provider_token: :obj:`str`

        :param currency: Three-letter ISO 4217 currency code,
            see https://core.telegram.org/bots/payments#supported-currencies
        :type currency: :obj:`str`

        :param prices: Price breakdown, a list of components
            (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        :type prices: List[:obj:`types.LabeledPrice`]

        :param start_parameter: Unique deep-linking parameter that can be used to generate this invoice
            when used as a start parameter
        :type start_parameter: :obj:`str`

        :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods
            or a marketing image for a service. People like it better when they see what they are paying for.
        :type photo_url: :obj:`str`

        :param photo_size: Photo size in bytes
        :type photo_size: :obj:`int`

        :param photo_width: Photo width 
        :type photo_width: :obj:`int`

        :param photo_height: Photo height
        :type photo_height: :obj:`int`

        :param need_name: Pass True, if you require the user's full name to complete the order
        :type need_name: :obj:`bool`

        :param need_phone_number: Pass True, if you require the user's phone number to complete the order
        :type need_phone_number: :obj:`bool`

        :param need_email: Pass True, if you require the user's email to complete the order
        :type need_email: :obj:`bool`

        :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
        :type need_shipping_address: :obj:`bool`

        :param is_flexible: Pass True, if the final price depends on the shipping method
        :type is_flexible: :obj:`bool`

        :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
        :type send_phone_number_to_provider: :obj:`bool`

        :param send_email_to_provider: Pass True, if user's email address should be sent to provider
        :type send_email_to_provider: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: A JSON-serialized object for an inline keyboard. If empty,
            one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button
        :type reply_markup: :obj:`str`

        :param provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider.
            A detailed description of required fields should be provided by the payment provider.
        :type provider_data: :obj:`str`

        :param timeout: Timeout of a request, defaults to None
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency
        :type max_tip_amount: :obj:`int`

        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the smallest
            units of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip
            amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        :type suggested_tip_amounts: :obj:`list` of :obj:`int`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :obj:`types.Message`
        """
        result = apihelper.send_invoice(
            self.token, chat_id, title, description, invoice_payload, provider_token,
            currency, prices, start_parameter, photo_url, photo_size, photo_width,
            photo_height, need_name, need_phone_number, need_email, need_shipping_address,
            send_phone_number_to_provider, send_email_to_provider, is_flexible, disable_notification,
            reply_to_message_id, reply_markup, provider_data, timeout, allow_sending_without_reply,
            max_tip_amount, suggested_tip_amounts, protect_content)
        return types.Message.de_json(result)

    def create_invoice_link(self,
            title: str, description: str, payload:str, provider_token: str, 
            currency: str, prices: List[types.LabeledPrice],
            max_tip_amount: Optional[int] = None, 
            suggested_tip_amounts: Optional[List[int]]=None,
            provider_data: Optional[str]=None,
            photo_url: Optional[str]=None,
            photo_size: Optional[int]=None,
            photo_width: Optional[int]=None,
            photo_height: Optional[int]=None,
            need_name: Optional[bool]=None,
            need_phone_number: Optional[bool]=None,
            need_email: Optional[bool]=None,
            need_shipping_address: Optional[bool]=None,
            send_phone_number_to_provider: Optional[bool]=None,
            send_email_to_provider: Optional[bool]=None,
            is_flexible: Optional[bool]=None) -> str:
            
        """
        Use this method to create a link for an invoice. 
        Returns the created invoice link as String on success.

        Telegram documentation:
        https://core.telegram.org/bots/api#createinvoicelink

        :param title: Product name, 1-32 characters
        :type title: :obj:`str`

        :param description: Product description, 1-255 characters
        :type description: :obj:`str`

        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
            use for your internal processes.
        :type payload: :obj:`str`

        :param provider_token: Payments provider token, obtained via @Botfather
        :type provider_token: :obj:`str`

        :param currency: Three-letter ISO 4217 currency code,
            see https://core.telegram.org/bots/payments#supported-currencies
        :type currency: :obj:`str`

        :param prices: Price breakdown, a list of components
            (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        :type prices: :obj:`list` of :obj:`types.LabeledPrice`

        :param max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency
        :type max_tip_amount: :obj:`int`

        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the smallest
            units of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip
            amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        :type suggested_tip_amounts: :obj:`list` of :obj:`int`

        :param provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider.
            A detailed description of required fields should be provided by the payment provider.
        :type provider_data: :obj:`str`

        :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods
            or a photo of the invoice. People like it better when they see a photo of what they are paying for.
        :type photo_url: :obj:`str`

        :param photo_size: Photo size in bytes
        :type photo_size: :obj:`int`

        :param photo_width: Photo width
        :type photo_width: :obj:`int`

        :param photo_height: Photo height
        :type photo_height: :obj:`int`

        :param need_name: Pass True, if you require the user's full name to complete the order
        :type need_name: :obj:`bool`

        :param need_phone_number: Pass True, if you require the user's phone number to complete the order
        :type need_phone_number: :obj:`bool`

        :param need_email: Pass True, if you require the user's email to complete the order
        :type need_email: :obj:`bool`

        :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
        :type need_shipping_address: :obj:`bool`

        :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
        :type send_phone_number_to_provider: :obj:`bool`

        :param send_email_to_provider: Pass True, if user's email address should be sent to provider
        :type send_email_to_provider: :obj:`bool`

        :param is_flexible: Pass True, if the final price depends on the shipping method
        :type is_flexible: :obj:`bool`

        :return: Created invoice link as String on success.
        :rtype: :obj:`str`
        """
        result = apihelper.create_invoice_link(
            self.token, title, description, payload, provider_token,
            currency, prices, max_tip_amount, suggested_tip_amounts, provider_data,
            photo_url, photo_size, photo_width, photo_height, need_name, need_phone_number,
            need_email, need_shipping_address, send_phone_number_to_provider,
            send_email_to_provider, is_flexible)
        return result

    def reply_to(self, message: types.Message, text: str, **kwargs) -> types.Message:
        """
        Convenience function for `send_message(message.chat.id, text, reply_to_message_id=message.message_id, **kwargs)`
        
        :param message: Instance of :class:`telebot.types.Message`
        :type message: :obj:`types.Message`

        :param text: Text of the message.
        :type text: :obj:`str`

        :param kwargs: Additional keyword arguments which are passed to :meth:`telebot.TeleBot.send_message`

        :return: On success, the sent Message is returned.
        :rtype: :class:`telebot.types.Message`
        """
        return self.send_message(message.chat.id, text, reply_to_message_id=message.message_id, **kwargs)

    def register_for_reply(self, message: types.Message, callback: Callable, *args, **kwargs) -> None:
        """
        Registers a callback function to be notified when a reply to `message` arrives.

        Warning: In case `callback` as lambda function, saving reply handlers will not work.

        :param message: The message for which we are awaiting a reply.
        :type message: :class:`telebot.types.Message`

        :param callback: The callback function to be called when a reply arrives. Must accept one `message`
            parameter, which will contain the replied message.
        :type callback: :obj:`Callable[[telebot.types.Message], None]`

        :param args: Optional arguments for the callback function.
        :param kwargs: Optional keyword arguments for the callback function.
        
        :return: None
        """
        message_id = message.message_id
        self.register_for_reply_by_message_id(message_id, callback, *args, **kwargs)

    def register_for_reply_by_message_id(
            self, message_id: int, callback: Callable, *args, **kwargs) -> None:
        """
        Registers a callback function to be notified when a reply to `message` arrives.

        Warning: In case `callback` as lambda function, saving reply handlers will not work.

        :param message_id: The id of the message for which we are awaiting a reply.
        :type message_id: :obj:`int`

        :param callback: The callback function to be called when a reply arrives. Must accept one `message`
            parameter, which will contain the replied message.
        :type callback: :obj:`Callable[[telebot.types.Message], None]`

        :param args: Optional arguments for the callback function.
        :param kwargs: Optional keyword arguments for the callback function.

        :return: None
        """
        self.reply_backend.register_handler(message_id, Handler(callback, *args, **kwargs))



    def register_next_step_handler(self, message: types.Message, callback: Callable, *args, **kwargs) -> None:
        """
        Registers a callback function to be notified when new message arrives after `message`.

        Warning: In case `callback` as lambda function, saving next step handlers will not work.

        :param message: The message for which we want to handle new message in the same chat.
        :type message: :class:`telebot.types.Message`

        :param callback: The callback function which next new message arrives.
        :type callback: :obj:`Callable[[telebot.types.Message], None]`

        :param args: Args to pass in callback func

        :param kwargs: Args to pass in callback func

        :return: None
        """
        chat_id = message.chat.id
        self.register_next_step_handler_by_chat_id(chat_id, callback, *args, **kwargs)


    def setup_middleware(self, middleware: BaseMiddleware):
        """
        Registers class-based middleware.

        :param middleware: Subclass of :class:`telebot.handler_backends.BaseMiddleware`
        :type middleware: :class:`telebot.handler_backends.BaseMiddleware`
        :return: None
        """
        if not self.use_class_middlewares:
            logger.error('Class-based middlewares are not enabled. Pass use_class_middlewares=True to enable it.')
            return

        if not hasattr(middleware, 'update_types'):
            logger.error('Middleware has no update_types parameter. Please add list of updates to handle.')
            return

        if not hasattr(middleware, 'update_sensitive'):
            logger.warning('Middleware has no update_sensitive parameter. Parameter was set to False.')
            middleware.update_sensitive = False

        self.middlewares.append(middleware)


    def set_state(self, user_id: int, state: Union[int, str, State], chat_id: Optional[int]=None) -> None:
        """
        Sets a new state of a user.

        .. note::

            You should set both user id and chat id in order to set state for a user in a chat.
            Otherwise, if you only set user_id, chat_id will equal to user_id, this means that
            state will be set for the user in his private chat with a bot.

        :param user_id: User's identifier
        :type user_id: :obj:`int`

        :param state: new state. can be string, integer, or :class:`telebot.types.State`
        :type state: :obj:`int` or :obj:`str` or :class:`telebot.types.State`

        :param chat_id: Chat's identifier
        :type chat_id: :obj:`int`

        :return: None
        """
        if chat_id is None:
            chat_id = user_id
        self.current_states.set_state(chat_id, user_id, state)

    def delete_state(self, user_id: int, chat_id: Optional[int]=None) -> None:
        """
        Delete the current state of a user.

        :param user_id: User's identifier
        :type user_id: :obj:`int`
        
        :param chat_id: Chat's identifier
        :type chat_id: :obj:`int`

        :return: None
        """
        if chat_id is None:
            chat_id = user_id
        self.current_states.delete_state(chat_id, user_id)


    def register_next_step_handler_by_chat_id(
            self, chat_id: Union[int, str], callback: Callable, *args, **kwargs) -> None:
        """
        Registers a callback function to be notified when new message arrives after `message`.

        Warning: In case `callback` as lambda function, saving next step handlers will not work.

        :param chat_id: The chat for which we want to handle new message.
        :type chat_id: :obj:`int` or :obj:`str`

        :param callback: The callback function which next new message arrives.
        :type callback: :obj:`Callable[[telebot.types.Message], None]`

        :param args: Args to pass in callback func
        
        :param kwargs: Args to pass in callback func

        :return: None
        """
        self.next_step_backend.register_handler(chat_id, Handler(callback, *args, **kwargs))


    def clear_step_handler(self, message: types.Message) -> None:
        """
        Clears all callback functions registered by register_next_step_handler().

        :param message: The message for which we want to handle new message after that in same chat.
        :type message: :class:`telebot.types.Message`

        :return: None
        """
        chat_id = message.chat.id
        self.clear_step_handler_by_chat_id(chat_id)

    def clear_step_handler_by_chat_id(self, chat_id: Union[int, str]) -> None:
        """
        Clears all callback functions registered by register_next_step_handler().

        :param chat_id: The chat for which we want to clear next step handlers
        :type chat_id: :obj:`int` or :obj:`str`

        :return: None
        """
        self.next_step_backend.clear_handlers(chat_id)

    def clear_reply_handlers(self, message: types.Message) -> None:
        """
        Clears all callback functions registered by register_for_reply() and register_for_reply_by_message_id().

        :param message: The message for which we want to clear reply handlers
        :type message: :class:`telebot.types.Message`

        :return: None
        """
        message_id = message.message_id
        self.clear_reply_handlers_by_message_id(message_id)

    def clear_reply_handlers_by_message_id(self, message_id: int) -> None:
        """
        Clears all callback functions registered by register_for_reply() and register_for_reply_by_message_id().

        :param message_id: The message id for which we want to clear reply handlers
        :type message_id: :obj:`int`

        :return: None
        """
        self.reply_backend.clear_handlers(message_id)

    def message_handler(self, commands: Optional[List[str]]=None, regexp: Optional[str]=None, func: Optional[Callable]=None,
                    content_types: Optional[List[str]]=None, chat_types: Optional[List[str]]=None, **kwargs):
        """
        Handles New incoming message of any kind - text, photo, sticker, etc.
        As a parameter to the decorator function, it passes :class:`telebot.types.Message` object.
        All message handlers are tested in the order they were added.

        Example:

        .. code-block:: python3
            :caption: Usage of message_handler

            bot = TeleBot('TOKEN')

            # Handles all messages which text matches regexp.
            @bot.message_handler(regexp='someregexp')
            def command_help(message):
                bot.send_message(message.chat.id, 'Did someone call for help?')

            # Handles messages in private chat
            @bot.message_handler(chat_types=['private']) # You can add more chat types
            def command_help(message):
                bot.send_message(message.chat.id, 'Private chat detected, sir!')

            # Handle all sent documents of type 'text/plain'.
            @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain',
                content_types=['document'])
            def command_handle_document(message):
                bot.send_message(message.chat.id, 'Document received, sir!')

            # Handle all other messages.
            @bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document',
                'text', 'location', 'contact', 'sticker'])
            def default_command(message):
                bot.send_message(message.chat.id, "This is the default command handler.")

        :param commands: Optional list of strings (commands to handle).
        :type commands: :obj:`list` of :obj:`str`

        :param regexp: Optional regular expression.
        :type regexp: :obj:`str`

        :param func: Optional lambda function. The lambda receives the message to test as the first parameter.
            It must return True if the command should handle the message.
        :type func: :obj:`lambda`

        :param content_types: Supported message content types. Must be a list. Defaults to ['text'].
        :type content_types: :obj:`list` of :obj:`str`

        :param chat_types: list of chat types
        :type chat_types: :obj:`list` of :obj:`str`

        :param kwargs: Optional keyword arguments(custom filters)

        :return: decorated function
        """
        if content_types is None:
            content_types = ["text"]

        method_name = "message_handler"

        if commands is not None:
            self.check_commands_input(commands, method_name)
            if isinstance(commands, str):
                commands = [commands]

        if regexp is not None:
            self.check_regexp_input(regexp, method_name)

        if isinstance(content_types, str):
            logger.warning("message_handler: 'content_types' filter should be List of strings (content types), not string.")
            content_types = [content_types]

        def decorator(handler):
            handler_dict = self._build_handler_dict(handler,
                                                    chat_types=chat_types,
                                                    content_types=content_types,
                                                    commands=commands,
                                                    regexp=regexp,
                                                    func=func,
                                                    **kwargs)
            self.add_message_handler(handler_dict)
            return handler

        return decorator

    def add_message_handler(self, handler_dict):
        """
        Adds a message handler
        Note that you should use register_message_handler to add message_handler to the bot.

        :meta private:

        :param handler_dict:
        :return:
        """
        self.message_handlers.append(handler_dict)

    def register_message_handler(self, callback: Callable, content_types: Optional[List[str]]=None, commands: Optional[List[str]]=None,
            regexp: Optional[str]=None, func: Optional[Callable]=None, chat_types: Optional[List[str]]=None, pass_bot: Optional[bool]=False, **kwargs):
        """
        Registers message handler.

        :param callback: function to be called
        :type callback: :obj:`function`

        :param content_types: Supported message content types. Must be a list. Defaults to ['text'].
        :type content_types: :obj:`list` of :obj:`str`

        :param commands: list of commands
        :type commands: :obj:`list` of :obj:`str`

        :param regexp:
        :type regexp: :obj:`str`

        :param func: Function executed as a filter
        :type func: :obj:`function`

        :param chat_types: List of chat types
        :type chat_types: :obj:`list` of :obj:`str`

        :param pass_bot: True if you need to pass TeleBot instance to handler(useful for separating handlers into different files)
        :type pass_bot: :obj:`bool`

        :param kwargs: Optional keyword arguments(custom filters)

        :return: None
        """
        method_name = "register_message_handler"

        if commands is not None:
            self.check_commands_input(commands, method_name)
            if isinstance(commands, str):
                commands = [commands]

        if regexp is not None:
            self.check_regexp_input(regexp, method_name)

        if isinstance(content_types, str):
            logger.warning("register_message_handler: 'content_types' filter should be List of strings (content types), not string.")
            content_types = [content_types]

        

        handler_dict = self._build_handler_dict(callback,
                                                chat_types=chat_types,
                                                content_types=content_types,
                                                commands=commands,
                                                regexp=regexp,
                                                func=func,
                                                pass_bot=pass_bot,
                                                **kwargs)
        self.add_message_handler(handler_dict)

    def inline_handler(self, func, **kwargs):
        """
        Handles new incoming inline query.
        As a parameter to the decorator function, it passes :class:`telebot.types.InlineQuery` object.

        :param func: Function executed as a filter
        :type func: :obj:`function`

        :param kwargs: Optional keyword arguments(custom filters)

        :return: None
        """
        def decorator(handler):
            handler_dict = self._build_handler_dict(handler, func=func, **kwargs)
            self.add_inline_handler(handler_dict)
            return handler

        return decorator

    def add_inline_handler(self, handler_dict):
        """
        Adds inline call handler
        Note that you should use register_inline_handler to add inline_handler to the bot.

        :meta private:

        :param handler_dict:
        :return:
        """
        self.inline_handlers.append(handler_dict)

    def register_inline_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool]=False, **kwargs):
        """
        Registers inline handler.

        :param callback: function to be called
        :type callback: :obj:`function`

        :param func: Function executed as a filter
        :type func: :obj:`function`

        :param pass_bot: True if you need to pass TeleBot instance to handler(useful for separating handlers into different files)
        :type pass_bot: :obj:`bool`

        :param kwargs: Optional keyword arguments(custom filters)

        :return: decorated function
        """
        handler_dict = self._build_handler_dict(callback, func=func, pass_bot=pass_bot, **kwargs)
        self.add_inline_handler(handler_dict)

    def chosen_inline_handler(self, func, **kwargs):
        """
        Handles the result of an inline query that was chosen by a user and sent to their chat partner.
        Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
        As a parameter to the decorator function, it passes :class:`telebot.types.ChosenInlineResult` object.

        :param func: Function executed as a filter
        :type func: :obj:`function`
        
        :param kwargs: Optional keyword arguments(custom filters)

        :return: None
        """
        def decorator(handler):
            handler_dict = self._build_handler_dict(handler, func=func, **kwargs)
            self.add_chosen_inline_handler(handler_dict)
            return handler

        return decorator

    def add_chosen_inline_handler(self, handler_dict):
        """
        Description: TBD
        Note that you should use register_chosen_inline_handler to add chosen_inline_handler to the bot.

        :meta private:

        :param handler_dict:
        :return:
        """
        self.chosen_inline_handlers.append(handler_dict)

    def register_chosen_inline_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool]=False, **kwargs):
        """
        Registers chosen inline handler.

        :param callback: function to be called
        :type callback: :obj:`function`

        :param func: Function executed as a filter
        :type func: :obj:`function`

        :param pass_bot: True if you need to pass TeleBot instance to handler(useful for separating handlers into different files)
        :type pass_bot: :obj:`bool`

        :param kwargs: Optional keyword arguments(custom filters)

        :return: None
        """
        handler_dict = self._build_handler_dict(callback, func=func, pass_bot=pass_bot, **kwargs)
        self.add_chosen_inline_handler(handler_dict)

    def callback_query_handler(self, func, **kwargs):
        """
        Handles new incoming callback query.
        As a parameter to the decorator function, it passes :class:`telebot.types.CallbackQuery` object.

        :param func: Function executed as a filter
        :type func: :obj:`function`

        :param kwargs: Optional keyword arguments(custom filters)
        
        :return: None
        """
        def decorator(handler):
            handler_dict = self._build_handler_dict(handler, func=func, **kwargs)
            self.add_callback_query_handler(handler_dict)
            return handler

        return decorator

    def add_callback_query_handler(self, handler_dict):
        """
        Adds a callback request handler
        Note that you should use register_callback_query_handler to add callback_query_handler to the bot.

        :meta private:

        :param handler_dict:
        :return:
        """
        self.callback_query_handlers.append(handler_dict)

    def register_callback_query_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool]=False, **kwargs):
        """
        Registers callback query handler.

        :param callback: function to be called
        :type callback: :obj:`function`

        :param func: Function executed as a filter
        :type func: :obj:`function`

        :param pass_bot: True if you need to pass TeleBot instance to handler(useful for separating handlers into different files)
        :type pass_bot: :obj:`bool`

        :param kwargs: Optional keyword arguments(custom filters)

        :return: None
        """
        handler_dict = self._build_handler_dict(callback, func=func, pass_bot=pass_bot, **kwargs)
        self.add_callback_query_handler(handler_dict)


# util.py


    def split_string(text: str, chars_per_string: int) -> List[str]:
        """
        Splits one string into multiple strings, with a maximum amount of `chars_per_string` characters per string.
        This is very useful for splitting one giant message into multiples.

        :param text: The text to split
        :type text: :obj:`str`

        :param chars_per_string: The number of characters per line the text is split into.
        :type chars_per_string: :obj:`int`

        :return: The splitted text as a list of strings.
        :rtype: :obj:`list` of :obj:`str`
        """
        return [text[i:i + chars_per_string] for i in range(0, len(text), chars_per_string)]


    def smart_split(text: str, chars_per_string: int=MAX_MESSAGE_LENGTH) -> List[str]:
        r"""
        Splits one string into multiple strings, with a maximum amount of `chars_per_string` characters per string.
        This is very useful for splitting one giant message into multiples.
        If `chars_per_string` > 4096: `chars_per_string` = 4096.
        Splits by '\n', '. ' or ' ' in exactly this priority.

        :param text: The text to split
        :type text: :obj:`str`

        :param chars_per_string: The number of maximum characters per part the text is split to.
        :type chars_per_string: :obj:`int`

        :return: The splitted text as a list of strings.
        :rtype: :obj:`list` of :obj:`str`
        """

        def _text_before_last(substr: str) -> str:
            return substr.join(part.split(substr)[:-1]) + substr

        if chars_per_string > MAX_MESSAGE_LENGTH: chars_per_string = MAX_MESSAGE_LENGTH

        parts = []
        while True:
            if len(text) < chars_per_string:
                parts.append(text)
                return parts

            part = text[:chars_per_string]

            if "\n" in part: part = _text_before_last("\n")
            elif ". " in part: part = _text_before_last(". ")
            elif " " in part: part = _text_before_last(" ")

            parts.append(part)
            text = text[len(part):]
