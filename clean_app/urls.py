from django.urls import path,include
from clean_app import views
urlpatterns = [

   path('forget_password/',views.forget_password),
   path('forget_password_post/',views.forget_password_post),

   # admin



   path('login/',views.login),
   path('login_post/',views.login_post),
   path('logout/',views.logout),
   path('admin_home/',views.admin_home),
   path('category/', views.category),
   path('category_post/',views.category_post),
   path('view_category/',views.view_category),
   path('view_category_post/',views.view_category_post),
   path('detele_category/<id>',views.detele_category),
   path('edit_category/<id>',views.edit_category),
   path('edit_category_post/',views.edit_category_post),
   path('recycle_reg/',views.recycle_reg),
   path('recycle_reg_post/',views.recycle_reg_post),
   path('recycle_aproved/<id>',views.recycle_aproved),
   path('worker_aproved/<id>',views.worker_aproved),
   path('reject_worker/<id>',views.reject_worker),
   path('view_reject_worker/',views.view_reject_worker),
   path('view_aproved_worker/',views.view_aproved_worker),
   path('view_aproved_worker_post/',views.view_aproved_worker_post),
   path('view_reject_worker_post/',views.view_reject_worker_post),
   path('view_recycle/',views.view_recycle),
   path('view_recycle_post/',views.view_recycle_post),
   path('recycle_reject/<int:id>',views.recycle_reject),
   path('view_aproved_recycler/',views.view_aproved_recycler),
   path('view_reject_recycler/',views.view_reject_recycler),
   path('waste/',views.waste),
   path('waste_post/', views.waste_post),
   path('view_waste/',views.view_waste),
   path('view_waste_post/',views.view_waste_post),
   path('delete_waste/<int:id>',views.delete_waste),
   path('wasteedit/<int:id>',views.wasteedit),
   path('wasteedit_post/',views.wasteedit_post),
   path('admin_change_password/',views.admin_change_password),
   path('admin_change_password_post/',views.admin_change_password_post),
   path('view_worker/',views.view_worker),
   path('view_worker_post/',views.view_worker_post),
   path('allocation/',views.allocation),
   path('view_allocation/',views.view_allocation),
   path('view_allocation_post/',views.view_allocation_post),
   path('edit_allocation/<id>',views.edit_allocation),
   path('edit_allocation_post/',views.edit_allocation_post),
   path('delete_allocation/<id>',views.delete_allocation),
   path('view_user/',views.view_user),
   path('view_user_post/',views.view_user_post),

   path('view_feedback/',views.view_feedback),
   path('view_feedback_post/',views.view_feedback_post),
   path('view_complaint/',views.view_complaint),
   path('view_complaint_post/',views.view_complaint_post),

   path('complaint_reply/<id>',views.complaint_reply),
   path('complaint_reply_post/',views.complaint_reply_post),
   path('allocation_post/',views.allocation_post),
   path('admin_view_notification/', views.admin_view_notification),
   path('admin_view_notification_post/', views.admin_view_notification_post),
   path('view_pickup/', views.view_pickup),
   path('view_pickup_post/', views.view_pickup_post),
   path('aproved_pickup/<id>', views.aproved_pickup),
   path('reject_pickup/<id>', views.reject_pickup),
   path('view_Aproved_pickup/', views.view_Aproved_pickup),
   path('view_Aproved_pickup_post/', views.view_Aproved_pickup_post),
   path('view_Reject_pickup/', views.view_Reject_pickup),
   path('view_Reject_pickup_post/', views.view_Reject_pickup_post),



   # worker
   path('worker_notification/',views.worker_notification),
   path('worker_notification_post/',views.worker_notification_post),
   path('delete_notification/<id>', views.delete_notification),
   # path('worker_view_user_request/',views.worker_view_user_requests),
   path('worker_reply__request_post/',views.worker_reply__request_post),







#    user
   path('user_profile/',views.user_profile),
   path('user_post/',views.user_post),
   path('edit_userprofile/',views.edit_userprofile),
   path('user_complaint_post/',views.user_complaint_post),
   path('login2/',views.login2),
   path('user_view_complaints/', views.user_view_complaints),
   path('add_waste_request/',views.add_waste_request),
   path('manage_feedback/',views.manage_feedback),
   path('user_view_feedback/',views.user_view_feedback),
   path('user_add_waste/',views.user_add_waste),
   path('viewrequestworker/',views.viewrequestworker),
   path('user_change_password/',views.user_change_password),
   path('view_recycle_product/', views.view_recycle_product),
   path('u_add_to_cart/',views.u_add_to_cart),
   path('view_cart/',views.view_cart),
   path('remove_cart/',views.remove_cart),
   path('user_forget_password/',views.user_forget_password),
   path('user_payment/',views.user_payment),
   path('view_order/',views.view_order),
   path('view_order_product/',views.view_order_product),
   path('user_logout/',views.user_logout),
   path('worker_category_request_sent/',views.worker_category_request_sent),
   path('view_worker_category_request/', views.view_worker_category_request),
   path('cancel_request/', views.cancel_request),
   path('view_waste_category/', views.view_waste_category),
   path('user_view_waste_request/', views.user_view_waste_request),
   path('waste_payment/', views.waste_payment),


    # worker
   path('worker_home/',views.worker_home),
   path('view_worker_category/',views.view_worker_category),
   path('worker_post/',views.worker_post),
   path('worker_profile/',views.worker_profile),
   path('view_worker_allocation/',views.view_worker_allocation),
   path('view_notification/',views.view_notification),
   path('view_worker_notification/',views.view_worker_notification),
   path('workerchangepassword/',views.workerchangepassword),
   # path('worker_view_user_request_and_reply/',views.worker_view_user_request_and_reply),
   path('worker_view_allocation/',views.worker_view_allocation),
   path('worker_view_user_request/',views.worker_view_user_request),
   path('worker_update_request/',views.worker_update_request),
   path('worker_update_status_request/', views.worker_update_status_request),
   path('worker_update_status_request_reject/', views.worker_update_status_request_reject),
   path('worker_edit_profile/', views.worker_edit_profile),

   # recycle
   path('recycle_home/',views.recycle_home),
   path('recycle/', views.recycle_reg),
   path('recycle_post/',views.recycle_reg_post),
   path('recycle_profile/',views.recycle_profile),
   path('recycler_edit_post/',views.recycler_edit_post),
   path('recycler_edit/<id>',views.recycler_edit),
   path('view_user_request/',views.view_user_request),
   path('product_view/',views.product_view),
   path('product_add/',views.product_add),
   path('product_add_post/',views.product_add_post),
   path('product_edit/<id>',views.product_edit),
   path('product_edit_post/',views.product_edit_post),
   path('product_delete/<id>',views.product_delete),
   path('view_reject_recycler_post/',views.view_reject_recycler_post),
   path('view_aproved_recycler_post/',views.view_aproved_recycler_post),
   path('recycle_change_password_post/',views.recycle_change_password_post),
   path('recycle_change_password/',views.recycle_change_password),
   path('recylcer_view_product_order/',views.recylcer_view_product_order),
   path('recylcer_view_ordersub/<id>',views.recylcer_view_ordersub),
   path('View_collected_user_request/',views.View_collected_user_request),



#    pickup
   path('pickup_post/', views.pickup_post),
   path('Pickup_edit_profile/', views.Pickup_edit_profile),
   path('pick_profile/', views.pick_profile),
   path('pickupchangepassword/', views.pickupchangepassword),
   path('view_user_waste_request/', views.view_user_waste_request),
   path('collect_waste_request/', views.collect_waste_request),

]
