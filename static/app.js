// 当文档加载完毕后
$(document).ready(function() {
    // 当点击“生成文本”按钮时
    $("#generate").click(function() {
        // 获取用户输入的Prompt
        var prompt = $("textarea[name='prompt']").val();

        // 向后端发送POST请求，生成文本
        $.ajax({
            url: '/generate_text',  // Flask应用的路由
            type: 'POST',  // 请求方法
            contentType: 'application/json',  // 内容类型
            data: JSON.stringify({'prompt': prompt}),  // 请求的数据
            success: function(data) {  // 请求成功后的回调
                // 显示生成的文本
                $("#generated-text").html(data['generated_text']);
            },
            error: function(xhr, status, error) {  // 请求失败时的回调
                console.error("Ajax request failed:", error);  // 打印错误信息
            }
        });
    });
});
