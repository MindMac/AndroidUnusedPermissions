#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Intent Permission Map

INTENT_PERMISSION_MAP = {
	'android.permission.BIND_WALLPAPER' : [ 
		'android.service.wallpaper.WallpaperService', 
	], 
	'com.android.launcher.permission.UNINSTALL_SHORTCUT' : [ 
		'com.android.launcher.action.UNINSTALL_SHORTCUT', 
	], 
	'android.permission.READ_PHONE_STATE' : [ 
		'android.intent.action.PHONE_STATE', 
	], 
	'com.android.launcher.permission.PRELOAD_WORKSPACE' : [ 
		'com.android.launcher.action.PRELOAD_WORKSPACE', 
	], 
	'android.permission.PROCESS_OUTGOING_CALLS' : [ 
		'android.intent.action.NEW_OUTGOING_CALL', 
	], 
	'android.permission.CALL_PRIVILEGED' : [ 
		'android.intent.action.CALL_EMERGENCY', 
		'android.intent.action.CALL_PRIVILEGED', 
	], 
	'android.permission.SHUTDOWN' : [ 
		'android.intent.action.ACTION_REQUEST_SHUTDOWN', 
		'android.intent.action.REBOOT', 
	], 
	'android.permission.BLUETOOTH' : [ 
		'android.bluetooth.adapter.action.REQUEST_DISCOVERABLE', 
		'android.bluetooth.adapter.action.REQUEST_ENABLE', 
		'android.bluetooth.headset.action.VENDOR_SPECIFIC_HEADSET_EVENT', 
		'android.bluetooth.device.action.BOND_STATE_CHANGED', 
		'android.bluetooth.pan.profile.action.CONNECTION_STATE_CHANGED', 
		'android.bluetooth.input.profile.action.CONNECTION_STATE_CHANGED', 
		'android.bluetooth.adapter.action.SCAN_MODE_CHANGED', 
		'android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED', 
		'android.bluetooth.a2dp.profile.action.CONNECTION_STATE_CHANGED', 
		'android.bluetooth.a2dp.profile.action.PLAYING_STATE_CHANGED', 
		'android.bluetooth.device.action.FOUND', 
		'android.bluetooth.device.action.DISAPPEARED', 
		'android.bluetooth.device.action.ACL_DISCONNECT_REQUESTED', 
		'android.bluetooth.adapter.action.LOCAL_NAME_CHANGED', 
		'android.bluetooth.adapter.action.SCAN_MODE_CHANGED', 
		'android.bluetooth.adapter.action.DISCOVERY_FINISHED', 
		'android.bluetooth.device.action.NAME_CHANGED', 
		'android.bluetooth.device.action.ALIAS_CHANGED', 
		'android.bluetooth.device.action.CLASS_CHANGED', 
		'android.bluetooth.device.action.ACL_DISCONNECTED', 
		'android.bluetooth.adapter.action.STATE_CHANGED', 
		'android.bluetooth.pbap.intent.action.PBAP_STATE_CHANGED', 
		'android.bluetooth.headset.profile.action.AUDIO_STATE_CHANGED', 
		'android.bluetooth.headset.profile.action.CONNECTION_STATE_CHANGED', 
	], 
	'android.permission.BLUETOOTH_ADMIN' : [ 
		'android.bluetooth.device.action.CONNECTION_ACCESS_CANCEL', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_REQUEST', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_REQUEST', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_REPLY', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_REQUEST', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_CANCEL', 
		'android.bluetooth.device.action.UUID', 
		'android.bluetooth.device.action.PAIRING_REQUEST', 
		'android.bluetooth.device.action.PAIRING_REQUEST', 
		'android.bluetooth.device.action.PAIRING_REQUEST', 
		'android.bluetooth.device.action.PAIRING_REQUEST', 
		'android.bluetooth.device.action.PAIRING_REQUEST', 
		'android.bluetooth.device.action.PAIRING_REQUEST', 
		'android.bluetooth.device.action.PAIRING_REQUEST', 
		'android.bluetooth.device.action.PAIRING_CANCEL', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_REQUEST', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_CANCEL', 
		'android.bluetooth.device.action.CONNECTION_ACCESS_REPLY', 
	], 
	'android.permission.NFC' : [ 
		'ndefine', 
	], 
	'android.permission.WRITE_CONTACTS' : [ 
		'com.android.contacts.VIEW_NOTIFICATION', 
	], 
	'android.permission.BIND_ACCESSIBILITY_SERVICE' : [ 
		'android.accessibilityservice.AccessibilityService', 
	], 
	'android.permission.BROADCAST_WAP_PUSH' : [ 
		'android.provider.Telephony.WAP_PUSH_RECEIVED', 
	], 
	'android.permission.BIND_TEXT_SERVICE' : [ 
		'android.service.textservice.SpellCheckerService', 
	], 
	'android.permission.BIND_VPN_SERVICE' : [ 
		'android.net.VpnService', 
	], 
	'com.android.frameworks.coretests.permission.TEST_GRANTED' : [ 
		'com.android.frameworks.coretests.activity.BROADCAST_LOCAL_GRANTED', 
		'com.android.frameworks.coretests.activity.BROADCAST_REMOTE_GRANTED', 
		'com.android.frameworks.coretests.activity.SERVICE_LOCAL_GRANTED', 
	], 
	'android.permission.SEND_SMS_NO_CONFIRMATION' : [ 
		'com.android.mms.intent.action.SENDTO_NO_CONFIRMATION', 
	], 
	'android.permission.BIND_INPUT_METHOD' : [ 
		'android.view.InputMethod', 
	], 
	'android.permission.MANAGE_ACCOUNTS' : [ 
		'android.intent.action.USER_SWITCHED', 
		'android.intent.action.USER_ADDED', 
		'android.intent.action.USER_REMOVED', 
	], 
	'android.permission.RECEIVE_BOOT_COMPLETED' : [ 
		'android.intent.action.BOOT_COMPLETED', 
	], 
	'android.app.cts.permission.TEST_GRANTED' : [ 
		'android.app.cts.activity.SERVICE_LOCAL_GRANTED', 
	], 
	'android.app.cts.permission.TEST_DENIED' : [ 
		'android.app.cts.activity.SERVICE_LOCAL_DENIED', 
	], 
	'com.android.permission.WHITELIST_BLUETOOTH_DEVICE' : [ 
		'android.btopp.intent.action.HANDOVER_SEND', 
		'android.btopp.intent.action.HANDOVER_SEND_MULTIPLE', 
		'android.btopp.intent.action.STOP_HANDOVER_TRANSFER', 
		'android.btopp.intent.action.WHITELIST_DEVICE', 
	], 
	'com.android.alarm.permission.SET_ALARM' : [ 
		'android.intent.action.SET_ALARM', 
	], 
	'android.permission.BIND_DEVICE_ADMIN' : [ 
		'android.app.action.DEVICE_ADMIN_ENABLED', 
	], 
	'android.permission.CALL_PHONE' : [ 
		'android.intent.action.CALL', 
	], 
	'android.permission.MASTER_CLEAR' : [ 
		'android.intent.action.MASTER_CLEAR', 
		'com.google.android.c2dm.intent.RECEIVE', 
	], 
	'com.android.browser.permission.PRELOAD' : [ 
		'android.intent.action.PRELOAD', 
	], 
	'com.android.frameworks.coretests.permission.TEST_DENIED' : [ 
		'com.android.frameworks.coretests.activity.BROADCAST_LOCAL_DENIED', 
		'com.android.frameworks.coretests.activity.BROADCAST_REMOTE_DENIED', 
		'com.android.frameworks.coretests.activity.SERVICE_LOCAL_DENIED', 
	], 
	'com.android.email.permission.ACCESS_PROVIDER' : [ 
		'com.android.email.ACCOUNT_INTENT', 
		'com.android.email.EXCHANGE_INTENT', 
		'com.android.email.POLICY_INTENT', 
	], 
	'android.permission.PERFORM_CDMA_PROVISIONING' : [ 
		'com.android.phone.PERFORM_CDMA_PROVISIONING', 
	], 
	'com.android.smspush.WAPPUSH_MANAGER_BIND' : [ 
		'com.android.internal.telephony.IWapPushManager', 
	], 
	'android.permission.BROADCAST_SMS' : [ 
		'android.provider.Telephony.SMS_CB_RECEIVED', 
		'android.provider.Telephony.SMS_EMERGENCY_CB_RECEIVED', 
		'android.provider.Telephony.SMS_RECEIVED', 
		'android.provider.Telephony.SMS_SERVICE_CATEGORY_PROGRAM_DATA_RECEIVED', 
	], 
	'com.android.launcher.permission.INSTALL_SHORTCUT' : [ 
		'com.android.launcher.action.INSTALL_SHORTCUT', 
	], 
	'android.permission.RECEIVE_SMS' : [ 
		'android.provider.Telephony.SIM_FULL', 
		'android.provider.Telephony.SMS_REJECTED', 
		'android.provider.Telephony.SMS_SERVICE_CATEGORY_PROGRAM_DATA_RECEIVED', 
		'android.provider.Telephony.SMS_RECEIVED', 
		'android.intent.action.DATA_SMS_RECEIVED', 
		'android.provider.Telephony.SMS_CB_RECEIVED', 
	], 
}