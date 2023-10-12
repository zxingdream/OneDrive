#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: leeyoshinari

class Msg(object):
    MsgParamError = '参数错误'
    MsgLoginSuccess = '{} 登陆成功'
    MsgLogoutSuccess = '{} 退出成功'
    MsgLoginFailure = '用户名或密码错误'
    MsgCreateUserSuccess = '用户 {} 创建成功'
    MsgCreateUserFailure = '用户 {} 创建失败'
    MsgExistUserError = '用户 {} 已存在'
    MsgModifyPwdSuccess = '{} 密码修改成功'
    MsgModifyPwdFailure = '{} 密码修改失败'
    MsgGetFileSuccess = '查询成功'
    MsgGetFileFailure = '查询失败'
    MsgFileTypeError = '不是标准的 {} 文件格式'
    MsgOperateSuccess = '操作成功'
    MsgOperateFailure = '操作失败'
    MsgSaveSuccess = '保存成功'
    MsgSaveFailure = '保存失败'
    MsgMoveSuccess = '移动成功'
    MsgMoveFailure = '移动失败'
    MsgUploadSuccess = '{} 上传成功'
    MsgFastUploadSuccess = '{} 快速上传成功'
    MsgUploadFailure = '{} 上传失败'
    MsgDownloadSuccess = '{} 下载成功'
    MsgDownloadFailure = '{} 下载失败'
    MsgCreateSuccess = '{} 创建成功'
    MsgCreateFailure = '{} 创建失败'
    MsgRenameSuccess = '{} 重命名成功'
    MsgRenameFailure = '{} 重命名失败'
    MsgDeleteSuccess = '{} 删除成功'
    MsgDeleteFailure = '{} 删除失败'
    MsgCopySuccess = '{} 复制成功'
    MsgCopyFailure = '{} 复制失败'
    MsgRestoreSuccess = '{} 还原成功'
    MsgRestoreFailure = '{} 还原失败'
    MsgNotFoundFileError = '本地不存在 {}'
    MsgFoundFileError = '本地已存在{}'
    MsgShareSuccess = '{} 分享成功'
    MsgShareFailure = '{} 分享失败'
    MsgShareOpen = '打开分享链接成功, 分享文件 {}'
    MsgExportError = '{} 文件夹里没有文件，导出失败'
    MsgAccessPermissionNon = '未经授权的访问'
