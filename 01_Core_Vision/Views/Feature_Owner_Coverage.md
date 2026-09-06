---
type: view
status: active
system: design_diagnostics
view_kind: feature_owner_coverage
upstream_sources:
  - "[[01_Core_Vision/Feature_Map]]"
navigation_role: "Feature_Owner_Coverage"
navigation_order: 4
navigation_label: "Feature × Owner: связи и пробелы"
---

# Feature × Owner

Производная диагностика читает `system_owners`, `ux_surfaces` и `validation` Feature-страниц и свойства активных систем. Наличие ссылки означает заявленную связь, а не проверенную совместимость. Отсутствие прямой связи у низкоуровневой системы — повод проверить её потребителей, а не автоматически удалить её.

![[01_Core_Vision/Views/Features.base]]

## Обратная карта и пропуски

```dataviewjs
const features = Array.from(dv.pages().where(p => p.type === "feature" && p.status === "active"))
    .sort((a,b) => (a.feature_order || 0) - (b.feature_order || 0));
const pathOf = link => dv.page(link)?.file.path;
const list = value => value ? Array.from(dv.array(value)) : [];
const reverse = new Map();
const invalid = [];
for (const feature of features) {
    for (const owner of list(feature.system_owners)) {
        const path = pathOf(owner);
        if (!path) { invalid.push([feature.file.link, String(owner)]); continue; }
        if (!reverse.has(path)) reverse.set(path, []);
        reverse.get(path).push(feature.file.link);
    }
}
dv.table(["Owner", "Features"], [...reverse.entries()].sort((a,b)=>a[0].localeCompare(b[0]))
    .map(([path, links]) => [dv.fileLink(path), links]));
dv.header(3, "Feature без UX или проверки");
const incomplete = features.filter(f => !list(f.ux_surfaces).length || !list(f.validation).length || !f.validation_state);
if (incomplete.length) dv.list(incomplete.map(f => f.file.link));
else dv.paragraph("У всех Features объявлены UX и проверка. Полнота сценариев требует чтения.");
dv.header(3, "Системы без прямой Feature-связи");
const indirect = Array.from(dv.pages().where(p => p.type === "system" && p.status === "active" && p.index_route === "owner"))
    .filter(p => !reverse.has(p.file.path));
if (indirect.length) dv.table(["System", "Входящие ссылки: проверьте косвенные потребители"], indirect.map(p => [p.file.link,p.file.inlinks]));
else dv.paragraph("Все активные системы имеют прямую Feature-связь.");
dv.header(3, "Число прямых зависимостей");
dv.table(["Feature", "Owners"], features.map(f => [f.file.link,list(f.system_owners).length]).sort((a,b)=>b[1]-a[1]));
dv.paragraph("Широкая Feature не обязательно ошибочна: проверьте цель игрока и competing state writers. Число ссылок не задаёт порог качества.");
if (invalid.length) dv.table(["Feature", "Неразрешённый owner"],invalid);
```
