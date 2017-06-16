odoo.define('warehouse.wave', function(require) {
    "use strict";
    var FormView = require('web.FormView');
    var form_relational = require('web.form_relational');
    var data = require('web.data');
    var Model = require('web.Model');
    var core = require('web.core');
    var Widget = require('web.Widget');

    var QWeb = core.qweb;
    var _t = core._t;

    FormView.include({
        start: function() {
            var self = this,
                res = this._super.apply(this, arguments);

            self.$el.on('keydown', '.do_pack_scan_code', function(event) {
                if (event.keyCode === 13) {
                    var $this = $(this);
                    return self.save().done(function(result) {
                        self.trigger("save", result);
                        self.reload().then(function() {
                            self.to_view_mode();
                            var menu = menu;
                            if (menu) {
                                menu.do_reload_needaction();
                            }
                        }).then(function() {
                            new Model("do.pack").call("scan_barcode", [self.model, $this.val(), self.datarecord.id]).then(
                                function() {
                                    self.reload();
                                    self.$el.find('input').val('');
                                }
                            );
                        }).then(function() {
                            $this.focus();
                        })
                    });
                }
            })
        },
    });

    function WarehouseWave(parent, action) {
        var self = this;
        new Model('wh.move').call('get_moves_html', [action.context.move_ids]).then(
            function(result) {
                var all_print = $("<div style='page-break-after:always;'></div>");
                for (var i = 0; i < result.length; i++) {
                    all_print.append($(result[i]));
                    all_print.append($("<div style='page-break-after:always;'></div>"));
                }
                all_print.jqprint({
                    debug: false, //如果是true则可以显示iframe查看效果（iframe默认高和宽都很小，可以再源码中调大），默认是false
                    importCSS: true, //true表示引进原来的页面的css，默认是true。（如果是true，先会找$("link[media=print]")，若没有会去找$("link")中的css文件）
                    printContainer: true, //表示如果原来选择的对象必须被纳入打印（注意：设置为false可能会打破你的CSS规则）。
                    operaSupport: false //表示如果插件也必须支持歌opera浏览器，在这种情况下，它提供了建立一个临时的打印选项卡。默认是true
                });
            })
    };
    core.action_registry.add('warehouse_wave.print_express_menu', WarehouseWave);
})