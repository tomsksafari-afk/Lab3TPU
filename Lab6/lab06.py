import sys
# ============================================================
# 01
# ============================================================
# class DraftComputer:
#     components: list[str] = []

#     def __init__(self, name):
#         self.name = name

# print("----------КОД С ОШИБКОЙ-------------")
# first = DraftComputer("Учебный ПК")
# second = DraftComputer("Сервер")
# first.components.append("SSD")
# print(first.components)
# print(second.components)
# print(first.components is second.components)


# class DraftComputerFixed:
#     def __init__(self, name, components: list[str]):
#         self.name = name
#         self.components = components

# print("-----------КОД ИСПРАВЛЕНЫЙ----------")
# first_fixed = DraftComputerFixed("Учебный ПК", [])
# second_fixed = DraftComputerFixed("Сервер", [])

# first_fixed.components.append("SSD")

# print(first_fixed.components)
# print(second_fixed.components)
# print(first_fixed.components is second_fixed.components)


# print("-----------ALIAS----------")
# alias = first
# alias.components.append("HDD")

# print(first.components)
# print(alias.components)
# print(first.components is alias.components)

# ============================================================
# 02
# ============================================================
# class DraftComputerFixed:
#     def __init__(self, name, components: list[str]):
#         self.name = name
#         self.components = components

#     def add_component(self, component):
#         self.components.append(component)


# first = DraftComputerFixed("Учебный ПК", [])
# second = DraftComputerFixed("Сервер", [])

# # 1. Обычный вызов метода и вызов через класс
# first.add_component("SSD")
# DraftComputerFixed.add_component(second, "SSD")

# print(first.components)
# print(second.components)

# # 2. Состояние экземпляра и динамический атрибут
# print(first.__dict__)

# first.room = "204"
# print(first.__dict__)

# # 3. Сохранённая ссылка на список
# saved = first.components
# first.add_component("HDD")
# print(saved)

# saved.append("USB")
# print(first.components)


# ============================================================
# 03-05
# ============================================================
class Computer:
    """Компьютер с памятью и списком компонентов."""

    def __init__(
        self,
        name: str,
        memory_gb: int,
    ) -> None:
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")

        name = name.strip()

        if not name:
            raise ValueError("Имя не может быть пустым")

        self.name = name
        self.memory_gb = memory_gb
        self._components: list[str] = []

    @property
    def memory_gb(self) -> int:
        return self._memory_gb

    @memory_gb.setter
    def memory_gb(self, value: int) -> None:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Память должна быть целым числом")

        if value <= 0:
            raise ValueError("Память должна быть положительной")

        self._memory_gb = value

    @property
    def components(self) -> tuple[str, ...]:
        return tuple(self._components)

    def add_component(self, component: str) -> None:
        if not isinstance(component, str):
            raise TypeError("Компонент должен быть строкой")

        component = component.strip()

        if not component:
            raise ValueError("Название компонента не может быть пустым")

        self._components.append(component)

    def remove_component(self, component: str) -> int:
        """Удаляет все компоненты с указанным названием."""

        if not isinstance(component, str):
            raise TypeError("Компонент должен быть строкой")

        component = component.strip()

        if not component:
            raise ValueError("Название компонента не может быть пустым")

        old_count = len(self._components)

        self._components = [item for item in self._components if item != component]

        return old_count - len(self._components)

    def __str__(self) -> str:
        return f"{self.name}: {self.memory_gb} ГБ, компонентов: {len(self._components)}"

    def __len__(self) -> int:
        return len(self._components)

    def __getitem__(self, index: int) -> str:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")

        return self._components[index]


pc = Computer("  Учебный ПК  ", 16)
pc.add_component(" SSD ")
saved = pc.components
pc.add_component("GPU")

assert pc.name == "Учебный ПК"
assert saved == ("SSD",)
assert pc.components == ("SSD", "GPU")
assert len(pc) == 2
assert pc[0] == "SSD"
assert pc[-1] == "GPU"
assert str(pc) == "Учебный ПК: 16 ГБ, компонентов: 2"

pc.memory_gb = 32
assert pc.memory_gb == 32

# ============================================================
# ТЕСТЫ
# ============================================================


def test_create_and_normalize() -> None:
    pc = Computer("  Учебный ПК  ", 16)

    assert pc.name == "Учебный ПК"
    assert pc.memory_gb == 16
    assert pc.components == ()
    assert len(pc) == 0


def test_independent_instances() -> None:
    pc1 = Computer("ПК 1", 16)
    pc2 = Computer("ПК 2", 32)

    pc1.add_component("GPU")

    assert pc1.components == ("GPU",)
    assert pc2.components == ()
    assert len(pc1) == 1
    assert len(pc2) == 0


def test_add_component_and_snapshot() -> None:
    pc = Computer("ПК", 16)

    pc.add_component("  HDD  ")
    saved = pc.components

    pc.add_component("GPU")
    pc.add_component("GPU")

    assert pc.components == ("HDD", "GPU", "GPU")
    assert saved == ("HDD",)


def test_str_len_and_indexes() -> None:
    pc = Computer("Учебный ПК", 16)

    pc.add_component("SSD")
    pc.add_component("GPU")

    assert str(pc) == "Учебный ПК: 16 ГБ, компонентов: 2"
    assert len(pc) == 2
    assert pc[0] == "SSD"
    assert pc[-1] == "GPU"

    try:
        pc[2]
    except IndexError:
        pass
    else:
        raise AssertionError("Ожидалось исключение IndexError")

    empty_pc = Computer("Пустой ПК", 16)

    try:
        empty_pc[0]
    except IndexError:
        pass
    else:
        raise AssertionError("Ожидалось исключение IndexError")


def test_correct_memory_change() -> None:
    pc = Computer("ПК", 16)

    pc.memory_gb = 32

    assert pc.memory_gb == 32


def test_invalid_memory() -> None:
    pc = Computer("ПК", 32)

    try:
        pc.memory_gb = 0
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    assert pc.memory_gb == 32

    try:
        pc.memory_gb = -8
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    assert pc.memory_gb == 32

    try:
        pc.memory_gb = "32"  # type: ignore[assignment]
    except TypeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение TypeError")

    assert pc.memory_gb == 32

    try:
        pc.memory_gb = True  # type: ignore[assignment]
    except TypeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение TypeError")

    assert pc.memory_gb == 32

    try:
        Computer("ПК", 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    try:
        Computer("ПК", -1)
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    try:
        Computer("ПК", "32")  # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение TypeError")

    try:
        Computer("ПК", True)  # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение TypeError")


def test_invalid_strings() -> None:
    try:
        Computer("   ", 16)
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    try:
        Computer("", 16)
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    try:
        Computer(123, 16)  # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение TypeError")

    pc = Computer("ПК", 16)
    pc.add_component("GPU")

    old_components = pc.components

    try:
        pc.add_component("   ")
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    assert pc.components == old_components

    try:
        pc.add_component(123)  # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение TypeError")

    assert pc.components == old_components


def test_components_read_only() -> None:
    pc = Computer("ПК", 16)

    pc.add_component("GPU")

    try:
        pc.components = ("SSD",)  # type: ignore[misc]
    except AttributeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение AttributeError")

    assert pc.components == ("GPU",)


def test_remove_component() -> None:
    pc = Computer("ПК", 16)

    pc.add_component("HDD")
    pc.add_component("HDD")
    pc.add_component("GPU")

    removed = pc.remove_component("HDD")

    assert removed == 2
    assert pc.components == ("GPU",)
    assert len(pc) == 1


def test_remove_component_special_cases() -> None:
    # Пустой компьютер
    pc = Computer("ПК", 16)

    removed = pc.remove_component("HDD")

    assert removed == 0
    assert pc.components == ()

    # Отсутствующий компонент
    pc.add_component("GPU")

    removed = pc.remove_component("HDD")

    assert removed == 0
    assert pc.components == ("GPU",)

    # Нормализация аргумента
    pc.add_component("HDD")
    pc.add_component("HDD")

    removed = pc.remove_component("  HDD  ")

    assert removed == 2
    assert pc.components == ("GPU",)

    # Пустая строка
    old_components = pc.components

    try:
        pc.remove_component("   ")
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    assert pc.components == old_components

    # Неверный тип
    try:
        pc.remove_component(123)  # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        raise AssertionError("Ожидалось исключение TypeError")

    assert pc.components == old_components


# ============================================================
# ЭКСПЕРИМЕНТ С __slots__
# ============================================================


class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SlottedPoint:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def slots_experiment():
    regular = RegularPoint(10, 20)
    slotted = SlottedPoint(10, 20)

    print()
    print("=== Эксперимент с __slots__ ===")
    print(f"Python: 3.13.5")

    # 1. Изменение существующего атрибута
    regular.x = 100
    slotted.x = 100

    print("1. Изменение x:")
    print(f"RegularPoint.x = {regular.x}")
    print(f"SlottedPoint.x = {slotted.x}")

    # 2. Новый атрибут xx
    print()
    print("2. Добавление нового атрибута xx:")

    regular.xx = 30
    print(f"RegularPoint.xx = {regular.xx}")

    try:
        slotted.xx = 30
    except AttributeError as error:
        print(f"{type(error)}")

    # 3. __dict__
    print()
    print("3. Наличие __dict__:")

    print(f"RegularPoint: {hasattr(regular, '__dict__')}")
    print(f"SlottedPoint: {hasattr(slotted, '__dict__')}")

    # 4. Строка в x
    print()
    print("4. Запись строки в x:")

    regular.x = "hello"
    slotted.x = "hello"

    print(f"RegularPoint.x = {regular.x}")
    print(f"SlottedPoint.x = {slotted.x}")

    # 5. Размеры
    print()
    print("5. Размеры:")

    regular_size = sys.getsizeof(regular)
    slotted_size = sys.getsizeof(slotted)

    print(f"RegularPoint: {regular_size} байт")
    print(f"SlottedPoint: {slotted_size} байт")

    if hasattr(regular, "__dict__"):
        print(f"__dict__ RegularPoint: {sys.getsizeof(regular.__dict__)} байт")


# ============================================================
# ЗАПУСК ВСЕХ ТЕСТОВ
# ============================================================


test_create_and_normalize()
test_independent_instances()
test_add_component_and_snapshot()
test_str_len_and_indexes()
test_correct_memory_change()
test_invalid_memory()
test_invalid_strings()
test_components_read_only()
test_remove_component()
test_remove_component_special_cases()

print("Все 10 тестов пройдены.")

slots_experiment()
