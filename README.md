System check identified no issues (0 silenced).
August 24, 2024 - 22:48:31
Django version 5.0.7, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Categories: <QuerySet [<Category: Мировые новости>]>
Subscribers: <QuerySet ['', 'jeckling@yandex.ru']>
Internal Server Error: /post/create/
Traceback (most recent call last):
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\contrib\auth\mixins.py", line 109, in dispatch
    return super().dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\base.py", line 143, in dispatch
    return handler(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\edit.py", line 182, in post
    return super().post(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\edit.py", line 151, in post
    return self.form_valid(form)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\views.py", line 81, in form_valid
    return super().form_valid(form)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\edit.py", line 133, in form_valid
    self.object = form.save()
                  ^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\forms\models.py", line 553, in save
    self._save_m2m()
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\forms\models.py", line 534, in _save_m2m
    f.save_form_data(self.instance, cleaned_data[f.name])
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related.py", line 1979, in save_form_data     
    getattr(instance, self.attname).set(data)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1300, in set    
    self.add(*new_objs, through_defaults=through_defaults)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1201, in add    
    self._add_items(
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1511, in _add_it
ems
    signals.m2m_changed.send(
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\dispatch\dispatcher.py", line 189, in send
    response = receiver(signal=self, sender=sender, **named)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py", line 20, in notify_subscribers
    message=f'Вот новые статьи за последнюю неделю: {message_content}',
                                                     ^^^^^^^^^^^^^^^
NameError: name 'message_content' is not defined
Internal Server Error: /post/create/
Traceback (most recent call last):
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\contrib\auth\mixins.py", line 109, in dispatch
    return super().dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\base.py", line 143, in dispatch
    return handler(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\edit.py", line 182, in post
    return super().post(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\edit.py", line 151, in post
    return self.form_valid(form)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\views.py", line 81, in form_valid
    return super().form_valid(form)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\views\generic\edit.py", line 133, in form_valid
    self.object = form.save()
                  ^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\forms\models.py", line 553, in save
    self._save_m2m()
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\forms\models.py", line 534, in _save_m2m
    f.save_form_data(self.instance, cleaned_data[f.name])
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related.py", line 1979, in save_form_data     
    getattr(instance, self.attname).set(data)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1300, in set    
    self.add(*new_objs, through_defaults=through_defaults)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1201, in add    
    self._add_items(
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1511, in _add_it
ems
    signals.m2m_changed.send(
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\dispatch\dispatcher.py", line 189, in send
    response = receiver(signal=self, sender=sender, **named)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py", line 20, in notify_subscribers
    message=f'Вот новые статьи за последнюю неделю: {message_content}',
                                                     ^^^^^^^^^^^^^^^
NameError: name 'message_content' is not defined
[24/Aug/2024 22:48:36] "POST /post/create/ HTTP/1.1" 500 134234
Looking for jobs to run
Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:49:00 +05)" (scheduled at 2024-08-24 22:49:00+05:00)    
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:49:00 +05)" (scheduled at 2024-08-24 22:49:00+05:00)    
Next wakeup is due at 2024-08-24 22:50:00+05:00 (in 59.719459 seconds)
Next wakeup is due at 2024-08-24 22:50:00+05:00 (in 59.593657 seconds)
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:50:00 +05)" executed successfully
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:50:00 +05)" executed successfully
Looking for jobs to run
Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:51:00 +05)" (scheduled at 2024-08-24 22:50:00+05:00)    
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:51:00 +05)" (scheduled at 2024-08-24 22:50:00+05:00)    
DB error executing 'update_job' (database is locked). Retrying with a new DB connection...
Next wakeup is due at 2024-08-24 22:51:00+05:00 (in 59.781755 seconds)
Exception in thread APScheduler:
Traceback (most recent call last):
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\sqlite3\base.py", line 329, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django_apscheduler\util.py", line 98, in func_wrapper
    result = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django_apscheduler\jobstores.py", line 258, in update_job
    db_job.save()
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 822, in save
    self.save_base(
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 909, in save_base
    updated = self._save_table(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 1040, in _save_table
    updated = self._do_update(
              ^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 1105, in _do_update
    return filtered._update(values) > 0
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\query.py", line 1278, in _update
    return query.get_compiler(self.db).execute_sql(CURSOR)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\sql\compiler.py", line 1990, in execute_sql
    cursor = super().execute_sql(result_type)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\sql\compiler.py", line 1562, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 122, in execute
    return super().execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers      
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\sqlite3\base.py", line 329, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.OperationalError: database is locked

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\sqlite3\base.py", line 329, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\s\AppData\Local\Programs\Python\Python311-32\Lib\threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "C:\Users\s\AppData\Local\Programs\Python\Python311-32\Lib\threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\apscheduler\schedulers\blocking.py", line 32, in _main_loop
    wait_seconds = self._process_jobs()
                   ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\apscheduler\schedulers\base.py", line 1009, in _process_jobs
    jobstore.update_job(job)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django_apscheduler\util.py", line 104, in func_wrapper
    result = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django_apscheduler\jobstores.py", line 258, in update_job
    db_job.save()
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 822, in save
    self.save_base(
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 909, in save_base
    updated = self._save_table(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 1040, in _save_table
    updated = self._do_update(
              ^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\base.py", line 1105, in _do_update
    return filtered._update(values) > 0
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\query.py", line 1278, in _update
    return query.get_compiler(self.db).execute_sql(CURSOR)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\sql\compiler.py", line 1990, in execute_sql
    cursor = super().execute_sql(result_type)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\models\sql\compiler.py", line 1562, in execute_sql
    cursor.execute(sql, params)
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 122, in execute
    return super().execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers      
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\sqlite3\base.py", line 329, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.OperationalError: database is locked
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:51:00 +05)" executed successfully
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:51:00 +05)" executed successfully
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py changed, reloading.
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py changed, reloading.
Looking up time zone info from registry
Adding job tentatively -- it will be properly scheduled when the scheduler starts
C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py:98: RuntimeWarning: Accessing the database during 
app initialization is discouraged. To fix this warning, avoid executing queries in AppConfig.ready() or when your app modules are imported.    
  warnings.warn(self.APPS_NOT_READY_WARNING_MSG, category=RuntimeWarning)
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
Next wakeup is due at 2024-08-24 22:51:00+05:00 (in 41.818063 seconds)
Watching for file changes with StatReloader
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2024 - 22:50:18
Django version 5.0.7, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Categories: <QuerySet [<Category: Мировые новости>]>
Subscribers: <QuerySet ['', 'jeckling@yandex.ru']>
Sent email to:
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject:
 =?utf-8?b?0J3QvtCy0YvQuSDQv9C+0YHRgiDQsiDQnNC40YDQvtCy0YvQtSDQvdC+0LLQvtGB?=
 =?utf-8?b?0YLQuA==?=
From: autotechsupp74@yandex.ru
To: jeckling@yandex.ru
Date: Sat, 24 Aug 2024 17:50:22 -0000
Message-ID: <172452182239.17548.5048499536419076646@delog.xn--n1aaa>

Вышел новый пост "Статья 13". Вы можете прочитать его по ссылке: http://127.0.0.1:8000/news/55/
-------------------------------------------------------------------------------
Sent email to: jeckling@yandex.ru
[24/Aug/2024 22:50:22] "POST /post/create/ HTTP/1.1" 302 0
[24/Aug/2024 22:50:22] "GET /news/ HTTP/1.1" 200 6009
[24/Aug/2024 22:50:22] "GET /static/js/scripts.js HTTP/1.1" 404 1798
Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:51:00 +05)" (scheduled at 2024-08-24 22:51:00+05:00)
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: =?utf-8?b?0JXQttC10L3QtdC00LXQu9GM0L3Ri9C5INC00LDQudC00LbQtdGB0YI=?=
From: autotechsupp74@yandex.ru
To: jeckling@yandex.ru
Date: Sat, 24 Aug 2024 17:51:00 -0000
Message-ID: <172452186012.17548.8604520691775939448@delog.xn--n1aaa>

Вот новые статьи за последнюю неделю:
Статья 13: http://127.0.0.1:8000/news/55/
-------------------------------------------------------------------------------
Next wakeup is due at 2024-08-24 22:52:00+05:00 (in 59.734410 seconds)
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:52:00 +05)" executed successfully
Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:53:00 +05)" (scheduled at 2024-08-24 22:52:00+05:00)
Next wakeup is due at 2024-08-24 22:53:00+05:00 (in 59.777976 seconds)
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:53:00 +05)" executed successfully
Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:54:00 +05)" (scheduled at 2024-08-24 22:53:00+05:00)
Next wakeup is due at 2024-08-24 22:54:00+05:00 (in 59.798024 seconds)
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:54:00 +05)" executed successfully
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\tasks.py changed, reloading.
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\tasks.py changed, reloading.
Looking up time zone info from registry
Adding job tentatively -- it will be properly scheduled when the scheduler starts
C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py:98: RuntimeWarning: Accessing the database during 
app initialization is discouraged. To fix this warning, avoid executing queries in AppConfig.ready() or when your app modules are imported.    
  warnings.warn(self.APPS_NOT_READY_WARNING_MSG, category=RuntimeWarning)
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
Next wakeup is due at 2024-08-24 22:54:00+05:00 (in 12.384045 seconds)
Watching for file changes with StatReloader
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2024 - 22:53:47
Django version 5.0.7, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[24/Aug/2024 22:53:52] "GET /post/create/ HTTP/1.1" 200 1541
Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:54:00 +05)" (scheduled at 2024-08-24 22:54:00+05:00)
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:55:00 +05)" executed successfully
Next wakeup is due at 2024-08-24 22:55:00+05:00 (in 59.521995 seconds)
Categories: <QuerySet [<Category: Мировые новости>]>
Subscribers: <QuerySet ['', 'jeckling@yandex.ru']>
Sent email to:
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: =?utf-8?b?TmV3IHBvc3QgaW4g0JzQuNGA0L7QstGL0LUg0L3QvtCy0L7RgdGC0Lg=?=
From: autotechsupp74@yandex.ru
To: jeckling@yandex.ru
Date: Sat, 24 Aug 2024 17:54:02 -0000
Message-ID: <172452204298.8584.1872466616749573787@delog.xn--n1aaa>

Вышел новый пост "Статья 15". Вы можете прочитать его по ссылке: http://127.0.0.1:8000/news/56/
-------------------------------------------------------------------------------
Sent email to: jeckling@yandex.ru
[24/Aug/2024 22:54:03] "POST /post/create/ HTTP/1.1" 302 0
[24/Aug/2024 22:54:03] "GET /news/ HTTP/1.1" 200 6011
[24/Aug/2024 22:54:03] "GET /static/js/scripts.js HTTP/1.1" 404 1798
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py changed, reloading.
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py changed, reloading.
Looking up time zone info from registry
Adding job tentatively -- it will be properly scheduled when the scheduler starts
C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py:98: RuntimeWarning: Accessing the database during 
app initialization is discouraged. To fix this warning, avoid executing queries in AppConfig.ready() or when your app modules are imported.    
  warnings.warn(self.APPS_NOT_READY_WARNING_MSG, category=RuntimeWarning)
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
Next wakeup is due at 2024-08-24 22:55:00+05:00 (in 26.588853 seconds)
Watching for file changes with StatReloader
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2024 - 22:54:33
Django version 5.0.7, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:55:00 +05)" (scheduled at 2024-08-24 22:55:00+05:00)
Next wakeup is due at 2024-08-24 22:56:00+05:00 (in 59.729543 seconds)
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: weekly digest
From: autotechsupp74@yandex.ru
To: jeckling@yandex.ru
Date: Sat, 24 Aug 2024 17:55:00 -0000
Message-ID: <172452210029.9012.7468206893143954775@delog.xn--n1aaa>

Вот новые статьи за последнюю неделю:
Статья 15: http://127.0.0.1:8000/news/56/
-------------------------------------------------------------------------------
Job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:56:00 +05)" executed successfully
[24/Aug/2024 22:55:12] "GET /post/create/ HTTP/1.1" 200 1541
Categories: <QuerySet [<Category: Мировые новости>]>
Subscribers: <QuerySet ['', 'jeckling@yandex.ru']>
Sent email to:
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: New post
From: autotechsupp74@yandex.ru
To: jeckling@yandex.ru
Date: Sat, 24 Aug 2024 17:55:18 -0000
Message-ID: <172452211892.9012.11802123758182681893@delog.xn--n1aaa>

Вышел новый пост "Статья 16". Вы можете прочитать его по ссылке: http://127.0.0.1:8000/news/57/
-------------------------------------------------------------------------------
Sent email to: jeckling@yandex.ru
[24/Aug/2024 22:55:19] "POST /post/create/ HTTP/1.1" 302 0
[24/Aug/2024 22:55:19] "GET /news/ HTTP/1.1" 200 6013
[24/Aug/2024 22:55:19] "GET /static/js/scripts.js HTTP/1.1" 404 1798
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py changed, reloading.
C:\Users\s\PycharmProjects\pythonProject6\project\newsapp\signals.py changed, reloading.
Looking up time zone info from registry
Adding job tentatively -- it will be properly scheduled when the scheduler starts
C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py:98: RuntimeWarning: Accessing the database during 
app initialization is discouraged. To fix this warning, avoid executing queries in AppConfig.ready() or when your app modules are imported.    
  warnings.warn(self.APPS_NOT_READY_WARNING_MSG, category=RuntimeWarning)
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
Next wakeup is due at 2024-08-24 22:56:00+05:00 (in 15.368153 seconds)
Watching for file changes with StatReloader
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2024 - 22:55:44
Django version 5.0.7, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Adding job tentatively -- it will be properly scheduled when the scheduler starts
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
Adding job tentatively -- it will be properly scheduled when the scheduler starts
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> py manage.py runserver
Looking up time zone info from registry
Adding job tentatively -- it will be properly scheduled when the scheduler starts
C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py:98: RuntimeWarning: Accessing the database during 
app initialization is discouraged. To fix this warning, avoid executing queries in AppConfig.ready() or when your app modules are imported.    
  warnings.warn(self.APPS_NOT_READY_WARNING_MSG, category=RuntimeWarning)
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
Next wakeup is due at 2024-08-24 22:57:00+05:00 (in 57.841955 seconds)
Looking up time zone info from registry
Adding job tentatively -- it will be properly scheduled when the scheduler starts
C:\Users\s\PycharmProjects\pythonProject6\venv\Lib\site-packages\django\db\backends\utils.py:98: RuntimeWarning: Accessing the database during 
app initialization is discouraged. To fix this warning, avoid executing queries in AppConfig.ready() or when your app modules are imported.    
  warnings.warn(self.APPS_NOT_READY_WARNING_MSG, category=RuntimeWarning)
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
Next wakeup is due at 2024-08-24 22:57:00+05:00 (in 56.833273 seconds)
Watching for file changes with StatReloader
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2024 - 22:56:03
Django version 5.0.7, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[24/Aug/2024 22:56:06] "GET /profile/ HTTP/1.1" 200 2053
[24/Aug/2024 22:56:06] "GET /static/js/scripts.js HTTP/1.1" 404 1798
[24/Aug/2024 22:56:07] "GET /accounts/logout/ HTTP/1.1" 200 1945
[24/Aug/2024 22:56:12] "GET /admin/ HTTP/1.1" 302 0
[24/Aug/2024 22:56:12] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 3679
[24/Aug/2024 22:56:14] "GET /admin/ HTTP/1.1" 302 0
[24/Aug/2024 22:56:14] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 3679
[24/Aug/2024 22:56:16] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[24/Aug/2024 22:56:16] "GET /admin/ HTTP/1.1" 200 15081
[24/Aug/2024 22:56:17] "GET /static/admin/img/icon-deletelink.svg HTTP/1.1" 200 392
[24/Aug/2024 22:56:19] "GET /admin/newsapp/post/ HTTP/1.1" 200 29015
[24/Aug/2024 22:56:19] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[24/Aug/2024 22:56:35] "POST /admin/newsapp/post/ HTTP/1.1" 200 15002
[24/Aug/2024 22:56:38] "POST /admin/newsapp/post/ HTTP/1.1" 302 0
[24/Aug/2024 22:56:38] "GET /admin/newsapp/post/ HTTP/1.1" 200 22463
[24/Aug/2024 22:56:38] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
Looking for jobs to run
Running job "send_weekly_digest (trigger: cron[minute='*'], next run at: 2024-08-24 22:57:00 +05)" (scheduled at 2024-08-24 22:57:00+05:00)
Looking for jobs to run
Next wakeup is due at 2024-08-24 22:58:00+05:00 (in 59.652714 seconds)
Next wakeup is due at 2024-08-24 22:58:00+05:00 (in 59.620543 seconds)
Looking for jobs to run
Scheduler started.
Adding job tentatively -- it will be properly scheduled when the scheduler starts
Added job "send_weekly_digest" to job store "default"
Scheduler started
Looking for jobs to run
Scheduler started.
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> git remote remove origin
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> git remote add origin https://github.com/delogen74/pythonproject6_d7.5.git        
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> git add .
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> git commit -m "nitial commit to the new repository"
[main 686644d] nitial commit to the new repository
 33 files changed, 396 insertions(+), 33 deletions(-)
 create mode 100644 newsapp/__pycache__/signals.cpython-311.pyc
 create mode 100644 newsapp/__pycache__/tasks.cpython-311.pyc
 create mode 100644 newsapp/management/commands/__pycache__/run_scheduler.cpython-311.pyc
 create mode 100644 newsapp/management/commands/run_scheduler.py
 create mode 100644 newsapp/migrations/0006_alter_category_name_subscriber.py
 create mode 100644 newsapp/migrations/0007_alter_category_name_alter_subscriber_category.py
 create mode 100644 newsapp/migrations/0008_rename_subscriber_subscription_alter_category_name.py
 create mode 100644 newsapp/migrations/0009_subscriber.py
 create mode 100644 newsapp/migrations/0011_digestrun.py
 create mode 100644 newsapp/migrations/__pycache__/0006_alter_category_name_subscriber.cpython-311.pyc
 create mode 100644 newsapp/migrations/__pycache__/0008_rename_subscriber_subscription_alter_category_name.cpython-311.pyc
 create mode 100644 newsapp/migrations/__pycache__/0010_delete_subscription.cpython-311.pyc
 create mode 100644 newsapp/migrations/__pycache__/0011_digestrun.cpython-311.pyc
 create mode 100644 newsapp/signals.py
 create mode 100644 newsapp/tasks.py
 create mode 100644 newsapp/templates/newsapp/subscriptions.html
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/delogen74/pythonproject6_d7.5.git'
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> git branch
* main
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> git push -u origin main
Enumerating objects: 212, done.
Counting objects: 100% (212/212), done.
Delta compression using up to 8 threads
Compressing objects: 100% (203/203), done.
Writing objects: 100% (212/212), 171.78 KiB | 4.09 MiB/s, done.
Total 212 (delta 82), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (82/82), done.
To https://github.com/delogen74/pythonproject6_d7.5.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(venv) PS C:\Users\s\PycharmProjects\pythonProject6\project> 
