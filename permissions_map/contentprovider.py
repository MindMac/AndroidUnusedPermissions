#!/usr/bin/env python
#-*- coding: utf-8 -*-

#ContentProvider Permission Map

CONTENTPROVIDER_PERMISSION_MAP = {
	'android.permission.READ_USER_DICTIONARY' : [ 
		'content://user_dictionary', 
	], 
	'android.permission.READ_CALENDAR' : [ 
		'content://com.android.calendar', 
	], 
	'com.android.voicemail.permission.ADD_VOICEMAIL' : [ 
		'content://com.android.voicemail', 
		'content://com.android.voicemail', 
	], 
	'android.permission.WRITE_CALENDAR' : [ 
		'content://com.android.calendar', 
	], 
	'android.permission.INTERNET' : [ 
		'content://downloads/download', 
		'content://downloads/download', 
		'content://downloads/my_downloads', 
		'content://downloads/my_downloads', 
	], 
	'com.android.cts.permissionNormal' : [ 
		'content://ctspermissionwithsignaturepathrestricting/foo/bar', 
	], 
	'android.permission.WRITE_CONTACTS' : [ 
		'content://com.android.contacts', 
		'content://contacts', 
		'content://icc', 
	], 
	'com.android.browser.permission.WRITE_HISTORY_BOOKMARKS' : [ 
		'content://browser', 
		'content://com.android.browser', 
	], 
	'android.permission.WRITE_SMS' : [ 
		'content://mms-sms', 
		'content://mms', 
		'content://sms', 
	], 
	'android.permission.ACCESS_BLUETOOTH_SHARE' : [ 
		'content://com.android.bluetooth.opp/btopp', 
		'content://com.android.bluetooth.opp/btopp', 
	], 
	'android.permission.WRITE_CALL_LOG' : [ 
		'content://call_log', 
	], 
	'android.permission.ACCESS_ALL_DOWNLOADS' : [ 
		'content://downloads/all_downloads', 
		'content://downloads/all_downloads', 
	], 
	'android.permission.READ_CALL_LOG' : [ 
		'content://call_log', 
	], 
	'com.android.browser.permission.READ_HISTORY_BOOKMARKS' : [ 
		'content://browser', 
		'content://com.android.browser.home', 
		'content://com.android.browser', 
	], 
	'android.permission.WRITE_EXTERNAL_STORAGE' : [ 
		'content://media/external/', 
	], 
	'android.permission.READ_EXTERNAL_STORAGE' : [ 
		'content://media/external/', 
	], 
	'com.android.email.permission.READ_ATTACHMENT' : [ 
		'content://com.android.email.attachmentprovider', 
	], 
	'android.permission.WRITE_USER_DICTIONARY' : [ 
		'content://user_dictionary', 
	], 
	'com.android.launcher.permission.READ_SETTINGS' : [ 
		'content://com.android.launcher2.settings', 
	], 
	'android.permission.READ_CELL_BROADCASTS' : [ 
		'content://cellbroadcasts', 
	], 
	'android.permission.WRITE_SETTINGS' : [ 
		'content://settings', 
	], 
	'android.permission.READ_SMS' : [ 
		'content://com.android.mms.SuggestionsProvider', 
		'content://mms', 
		'content://mms-sms', 
		'content://sms', 
	], 
	'com.android.email.permission.ACCESS_PROVIDER' : [ 
		'content://com.android.email.notifier', 
		'content://com.android.email.notifier', 
		'content://com.android.email.provider', 
		'content://com.android.email.provider', 
	], 
	'android.permission.GLOBAL_SEARCH' : [ 
		'content://browser/bookmarks/search_suggest_query', 
		'content://com.android.browser/bookmarks/search_suggest_query', 
		'content://com.android.contacts/contacts/.*/photo', 
		'content://com.android.contacts/search_suggest_query', 
		'content://com.android.contacts/search_suggest_shortcut', 
		'content://com.android.mms.SuggestionsProvider/search_suggest_query', 
		'content://com.android.mms.SuggestionsProvider/search_suggest_shortcut', 
		'content://contacts/contacts/.*/photo', 
		'content://contacts/search_suggest_query', 
		'content://contacts/search_suggest_shortcut', 
	], 
	'com.android.cts.permissionNotUsedWithSignature' : [ 
		'content://ctspermissionwithsignaturepath', 
		'content://ctspermissionwithsignaturepath', 
	], 
	'com.android.cts.permissionWithSignature' : [ 
		'content://ctspermissionwithsignaturegranting', 
		'content://ctspermissionwithsignaturegranting', 
		'content://ctspermissionwithsignaturepath/foo', 
		'content://ctspermissionwithsignaturepathrestricting/foo', 
		'content://ctspermissionwithsignaturepath/yes', 
		'content://ctspermissionwithsignature', 
		'content://ctspermissionwithsignature', 
	], 
	'com.android.launcher.permission.WRITE_SETTINGS' : [ 
		'content://com.android.launcher2.settings', 
	], 
	'android.permission.READ_CONTACTS' : [ 
		'content://com.android.contacts', 
		'content://com.android.exchange.directory.provider', 
		'content://contacts', 
		'content://icc', 
	], 
}